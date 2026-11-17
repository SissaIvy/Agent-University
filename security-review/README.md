# Security review tooling

`inventory_skill_json.py` inventories every `*.skill.json` under the repo root.

It reports package format, top-level keys, packaged path patterns (flags `..` / absolute / UNC), tool-grant key presence, packaged file extensions, and whether decoded payloads match secret-value or executable heuristics. It never prints secret values.

```bash
python3 security-review/inventory_skill_json.py --summary-only
python3 security-review/inventory_skill_json.py --json-out security-review/skill-json-inventory.json --summary-only
python3 security-review/inventory_skill_json.py --json-out security-review/skill-json-inventory-full.json
```

Generated JSON artifacts in this folder are metadata-only (no packaged file bodies).
