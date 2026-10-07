# DE-STU-004: StarNet agent context

**Data Engineering Student 04**, specialization **Data Quality & Reliability**, in Agents University's Data Engineering cohort DE-2026-09-29. Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus three shared skill packages. The other nine students have sibling folders (`../de-stu-0NN/`), and `../de-stu-all.zip` bundles all ten.

Source material: the `aml` repo, mainly `agents/cohorts/DE-2026-09-29/DE-STU-004/agent.json`, `cohort.json`, `agents/faculty/data-engineering/` (curriculum, pedagogy, thesis contract), and `ops/academic/matriculation/DE-2026-09-29.imhotep.json`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name `DE-STU-004`, the purpose line (123 chars), and the persona (appended under the station identity) | 3.3k / 16k |
| `AGENTS.md` | Standing orders: verbatim University rules and constraints, module procedure, specialty anchors, peer review, transfer, thesis contribution | 6.5k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context: the Commander's role, cohort roster, my status, derived defaults | 3,539 / 8,000 chars composed |
| `skills/*.skill.json` | Shared per-agent skills (`open-agent-skill-package/v1`), identical across all ten students | 3 packages |
| `skills-src/` | Readable source of those packages (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model. Pin one later in the dossier if wanted.

### Shared skills (same bytes and digests for every student)
- `de-curriculum`: the ten modules (objectives, required artifacts), evaluation dimensions, critical-failure rule, completion rule.
- `de-module-work`: the Reverse Scaffold procedure, failure injection, submission manifest (with no score field), peer review, transfer challenge.
- `de-cohort-thesis`: the thesis contract, 15 required sections with a derived ownership map, contribution and defense rules, how IMHOTEP validates.

### What is derived rather than sourced
The University record gives each student only an ID, a name and a specialization label; the system prompt and constraints are otherwise identical. What makes DE-STU-004 distinct was **derived** from the curriculum and the thesis contract, and is labelled as derived in the files:
- Specialty lens and stance.
- Anchor modules: DE700, DE300.
- Thesis sections: data_quality_observability_and_lineage, failure_injection_and_recovery.
- Peer-review pairing: reviews DE-STU-008; reviewed by DE-STU-001.
- Transfer principle.

The professor may override any of it.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/de-stu-004/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE DE-STU-004** in the detect list.
2. **Check the preview.** You should see name DE-STU-004, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With DE-STU-004 as the active agent, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**. Skills install per agent, so repeat for each student.

## Known limits

- StarNet cannot enforce evaluator independence or record module results. The rules are carried as standing orders, and submissions and evaluations are still recorded by `scripts/data_engineering_cohort.py` in `aml`.
- University status (MATRICULATED / UNASSESSED / DE100) is context only on the station.

## Validation (2026-10-07)

Validated against StarNet `feat/harness-backend@764fcfc8b` in a scratch copy (`/tmp/starnet-scratch`); the repo itself was not modified.

- **Pure engine:** 13/13 checks passed for DE-STU-004, and 132/132 across the cohort including the cross-student checks.
  - The scan returns ok with all 4 sources, no warnings, and nothing truncated.
  - The name passes the agent-name check.
  - The purpose is 123 chars (limit 140), and the composed context is 3,539 chars (limit 8,000).
  - All 3 skills pass the guard as `allow`.
  - The shared skill digests are identical across all ten students, and the ten purposes are all distinct.
- **Live sidecar:**
  - `/api/harness/detect` listed all 10 student profiles.
  - `/api/harness/scan` for DE-STU-004 returned ok, with all four docs byte-identical to the files.
  - `/api/skill-exchange/import` then `/install` succeeded for all 3 skills (guard `allow`), and `/api/agent-skills?agent=de-stu-004` shows them installed and not withheld.
- **Not exercised:** the browser RECRUIT click. Its purpose, context and name derivations were re-implemented from `marketplace.js` and checked.
