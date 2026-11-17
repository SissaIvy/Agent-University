# Agent-University security review — 2026-11-17

HEAD: `26c95aff1de80f9736de0e44ff058b818afdcbbb`  
Repo: `SissaIvy/Agent-University` (public; `has_pages: false`; 0 Actions workflows)

## NEW MEDIUM+ findings

**None.** Reconfirmed already-flagged items only; no distinct new MEDIUM+ chain.

### Already flagged (not new)

1. **HIGH** — Sealed DCTR hidden-exam policy publicly committed (`dctr-hidden-scenario` SKILL.md / policy JSON / installable `.skill.json`). Unauthenticated `raw.githubusercontent.com` still HTTP 200.
2. **MEDIUM** — Shared-station unsigned isolation / advisory RBAC (procedural self-discipline; unsigned evaluation/gate/evidence files).

## Skill JSON inventory (summary)

| Metric | Result |
|---|---|
| Packages | 57 |
| Format | `open-agent-skill-package/v1` (all) |
| Top keys | `format`, `digest`, `bytes`, `metadata`, `files` (all) |
| Packaged files | 118 |
| Extensions | `.md` 57, `.json` 57, `.csv` 4 |
| Path `..` / absolute | **0** |
| Tool grants | **0** |
| Secret-valueish decoded payloads | **0** |
| Embedded executables / exec hints | **0** |
| Unique digests | 19 (6 shared across agents) |

Run: `python3 security-review/inventory_skill_json.py --summary-only`

## Below bar / not elevated

- Apprentice ↔ Dean byte-identical `university-promotion-governance` (`digest` `b67d512d…`); shared by design, GO still needs Commander-run badges.
- A09 / evaluator threshold prose outside hidden-scenario overlaps flagged #1 rather than a new chain.
- Skill-guard A06 rename to `Model/Evaluation` so guard returns `allow` (author-side linter gaming; operator still installs).
- Learner/teacher public `dctr-protocol` disclosing concept + teach surface (intended public; omits hidden surface).
- Unsigned `evaluator_id` / `professor_id` string checks — same class as flagged #2.
- IMHOTEP write restrictions are self-discipline (same class as flagged #2).
- Thesis `section-ownership` is advisory mapping.
- Codespace skill binds `forwardPorts` to `127.0.0.1`; no `docker.sock` / `0.0.0.0`.
- `/api/harness/*` and `/api/skill-exchange/*` are scratch-validation notes, not live remote endpoints in this tree.
- No GitHub Actions, IAM, Terraform, Dockerfiles, or executable app code in-tree.
- Guessed Streamlit Cloud hostnames redirect-loop; no public app body. GitHub Pages 404.
- Students `de-stu-001..010` only have curriculum / module-work / cohort-thesis; privileged slugs stay on owners.

## Infra / live URL checks

- `visibility: public`, Pages 404, workflows: 0, releases/tags: none observed in prior/this scan scope.
- Sealed SKILL.md + `security_mastery_dctr.v1.1.json` still world-readable via raw GitHub (flagged #1).
