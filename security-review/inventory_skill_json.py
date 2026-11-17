#!/usr/bin/env python3
"""Inventory all *.skill.json packages in Agent-University.

Reports format, keys, packaged path patterns, tool grants, extensions,
and whether decoded content matches secret/executable heuristics.
Never prints secret *values* — names/locations/flags only.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

SECRET_NAME_RE = re.compile(
    r"(?i)(api[_-]?key|secret|password|passwd|private[_-]?key|access[_-]?token|"
    r"auth[_-]?token|bearer\s+[A-Za-z0-9\-._~+/]+=*|ghp_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
)
# Avoid false positives on instructional "no secrets" prose by requiring value-like shapes
SECRET_VALUEISH_RE = re.compile(
    r"(?i)("
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    r"ghp_[A-Za-z0-9]{36,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|"
    r"\bsk-[A-Za-z0-9]{20,}\b|"
    r"\bAKIA[0-9A-Z]{16}\b|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}|"
    r"Bearer\s+[A-Za-z0-9\-._~+/]{20,}="
    r")"
)
EXEC_HINT_RE = re.compile(
    r"(?i)(\beval\s*\(|\bexec\s*\(|\bsubprocess\b|\bos\.system\b|shell=True|"
    r"pickle\.loads|yaml\.load\s*\(|child_process|docker\.sock|"
    r"\b0\.0\.0\.0\b|#!/bin/|MZ\x00\x00|\x7fELF)"
)
TOOL_GRANT_KEYS = {
    "tools",
    "tool",
    "capabilities",
    "grants",
    "permissions",
    "mcp",
    "mcpServers",
    "allowed_tools",
    "tool_grants",
}


def is_traversal_or_abs(path: str) -> dict[str, bool]:
    p = path.replace("\\", "/")
    return {
        "has_dotdot": ".." in p.split("/"),
        "is_absolute": p.startswith("/") or (len(p) > 1 and p[1] == ":"),
        "is_unc": p.startswith("//"),
    }


def decode_file_entry(entry: dict[str, Any]) -> bytes:
    enc = entry.get("encoding", "utf-8")
    content = entry.get("content", "")
    if enc == "base64":
        return base64.b64decode(content)
    if isinstance(content, str):
        return content.encode("utf-8", errors="replace")
    if isinstance(content, bytes):
        return content
    return json.dumps(content).encode("utf-8")


def scan_decoded(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8", errors="replace")
    secret_hits = [m.group(0)[:12] + "…" for m in SECRET_VALUEISH_RE.finditer(text)]
    # Deduplicate pattern names only (never full match beyond short prefix)
    secret_patterns = sorted({m.re.pattern[:40] for m in SECRET_VALUEISH_RE.finditer(text)})
    exec_hits = sorted({m.group(0) for m in EXEC_HINT_RE.finditer(text)})
    # ELF/PE magic
    magic = []
    if data[:4] == b"\x7fELF":
        magic.append("ELF")
    if data[:2] == b"MZ":
        magic.append("PE/MZ")
    if data[:4] == b"\x00asm":
        magic.append("WASM")
    return {
        "secret_valueish_count": len(secret_hits),
        "secret_valueish_prefixes": secret_hits[:5],
        "exec_hint_matches": exec_hits[:10],
        "binary_magic": magic,
        "looks_executable": bool(magic) or any(
            x in exec_hits for x in ("#!/bin/", "\x7fELF", "MZ")
        ),
    }


def collect_tool_grant_keys(obj: Any, found: set[str], path: str = "") -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in TOOL_GRANT_KEYS:
                found.add(f"{path}.{k}" if path else k)
            collect_tool_grant_keys(v, found, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            collect_tool_grant_keys(v, found, f"{path}[{i}]")


def inventory_one(path: Path) -> dict[str, Any]:
    rel = str(path.relative_to(ROOT))
    raw = path.read_bytes()
    try:
        pkg = json.loads(raw)
    except json.JSONDecodeError as e:
        return {"path": rel, "error": f"json_decode: {e}"}

    top_keys = list(pkg.keys()) if isinstance(pkg, dict) else []
    tool_keys: set[str] = set()
    if isinstance(pkg, dict):
        collect_tool_grant_keys(pkg, tool_keys)

    files_out = []
    ext_counter: Counter[str] = Counter()
    path_issues = []
    decoded_secret = False
    decoded_exec = False
    decoded_exec_hints: list[str] = []

    for entry in pkg.get("files", []) if isinstance(pkg, dict) else []:
        fpath = entry.get("path", "")
        flags = is_traversal_or_abs(fpath)
        if any(flags.values()):
            path_issues.append({"path": fpath, **flags})
        ext = Path(fpath).suffix.lower() or "(none)"
        ext_counter[ext] += 1
        try:
            data = decode_file_entry(entry)
        except Exception as e:  # noqa: BLE001
            files_out.append({"path": fpath, "decode_error": str(e)})
            continue
        scan = scan_decoded(data)
        if scan["secret_valueish_count"]:
            decoded_secret = True
        if scan["looks_executable"] or scan["exec_hint_matches"] or scan["binary_magic"]:
            decoded_exec = True
            decoded_exec_hints.extend(scan["exec_hint_matches"])
            decoded_exec_hints.extend(scan["binary_magic"])
        files_out.append(
            {
                "path": fpath,
                "encoding": entry.get("encoding"),
                "bytes": entry.get("bytes"),
                "sha256": entry.get("sha256"),
                "ext": ext,
                "path_flags": flags,
                "secret_valueish_count": scan["secret_valueish_count"],
                "exec_hint_matches": scan["exec_hint_matches"],
                "binary_magic": scan["binary_magic"],
            }
        )

    return {
        "path": rel,
        "agent": path.parts[-3] if len(path.parts) >= 3 else None,
        "slug_guess": path.name.replace(".skill.json", ""),
        "format": pkg.get("format") if isinstance(pkg, dict) else None,
        "digest": pkg.get("digest") if isinstance(pkg, dict) else None,
        "bytes": pkg.get("bytes") if isinstance(pkg, dict) else None,
        "top_keys": top_keys,
        "metadata": pkg.get("metadata") if isinstance(pkg, dict) else None,
        "file_count": len(files_out),
        "extensions": dict(ext_counter),
        "path_issues": path_issues,
        "tool_grant_keys": sorted(tool_keys),
        "has_tool_grants": bool(tool_keys),
        "decoded_contains_secret_valueish": decoded_secret,
        "decoded_contains_executable_hints": decoded_exec,
        "decoded_exec_hint_samples": sorted(set(decoded_exec_hints))[:20],
        "files": files_out,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--json-out", type=Path, default=None)
    ap.add_argument("--summary-only", action="store_true")
    args = ap.parse_args()
    root: Path = args.root

    skills = sorted(root.rglob("*.skill.json"))
    records = [inventory_one(p) for p in skills]

    formats = Counter(r.get("format") for r in records)
    all_top_keys = Counter(tuple(r.get("top_keys") or []) for r in records)
    all_exts: Counter[str] = Counter()
    for r in records:
        for e, n in (r.get("extensions") or {}).items():
            all_exts[e] += n
    digests = defaultdict(list)
    for r in records:
        if r.get("digest"):
            digests[r["digest"]].append(r["path"])

    summary = {
        "repo_root": str(root),
        "skill_package_count": len(records),
        "formats": {str(k): v for k, v in formats.items()},
        "top_key_shapes": [
            {"keys": list(k), "count": v} for k, v in all_top_keys.most_common()
        ],
        "packaged_file_total": sum(r.get("file_count") or 0 for r in records),
        "extensions": dict(all_exts),
        "packages_with_path_issues": [
            {"path": r["path"], "issues": r["path_issues"]}
            for r in records
            if r.get("path_issues")
        ],
        "packages_with_tool_grants": [
            {"path": r["path"], "tool_grant_keys": r.get("tool_grant_keys")}
            for r in records
            if r.get("has_tool_grants")
        ],
        "packages_with_secret_valueish": [
            r["path"] for r in records if r.get("decoded_contains_secret_valueish")
        ],
        "packages_with_executable_hints": [
            {
                "path": r["path"],
                "hints": r.get("decoded_exec_hint_samples"),
            }
            for r in records
            if r.get("decoded_contains_executable_hints")
        ],
        "unique_digest_count": len(digests),
        "shared_digests": [
            {"digest": d[:16] + "…", "count": len(paths), "paths": paths}
            for d, paths in sorted(digests.items(), key=lambda x: -len(x[1]))
            if len(paths) > 1
        ],
        "by_agent": {
            agent: sorted({r["slug_guess"] for r in records if r.get("agent") == agent})
            for agent in sorted({r.get("agent") for r in records if r.get("agent")})
        },
    }

    out = {"summary": summary, "packages": records if not args.summary_only else None}
    if args.summary_only:
        out.pop("packages")

    text = json.dumps(out, indent=2, sort_keys=False)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {args.json_out}", file=sys.stderr)

    # Human summary to stdout (no package payloads)
    s = summary
    print(f"skill_packages={s['skill_package_count']}")
    print(f"formats={s['formats']}")
    print(f"top_key_shapes={s['top_key_shapes']}")
    print(f"packaged_files={s['packaged_file_total']} extensions={s['extensions']}")
    print(f"path_issues={len(s['packages_with_path_issues'])}")
    print(f"tool_grants={len(s['packages_with_tool_grants'])}")
    print(f"secret_valueish={len(s['packages_with_secret_valueish'])}")
    print(f"executable_hints={len(s['packages_with_executable_hints'])}")
    print(f"unique_digests={s['unique_digest_count']} shared={len(s['shared_digests'])}")
    for row in s["packages_with_executable_hints"]:
        print(f"  exec_hint: {row}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
