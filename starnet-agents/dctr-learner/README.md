# DCTR-Learner: StarNet agent context

The DCTR **learner** role (University id `LRN.cohort.executor`), packaged as a **Hermes agent home** for StarNet's **Import Agent** flow. Siblings: `../dctr-teacher/`, `../dctr-learner/`, `../dctr-evaluator/`, `../dctr-gatekeeper/`, `../dctr-scenario-gen/`; `../dctr-all.zip` bundles all five.

Source material (the `aml` repo): `policies/security_mastery_dctr.v1.1.json`, `policies/experimental_cohort_controller.v1.json`, `policies/security_mastery_game.v1.json`, `scripts/security_games_dctr.py`, `scripts/a09_promotion_gate.py`, `scripts/experimental_cohort_controller.py`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **DCTR-LEARNER**, purpose line (129 chars), persona | 1.4k / 16k |
| `AGENTS.md` | Standing orders, isolation matrix, critical failure codes | 3.5k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 2,737 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 2 |
| `skills-src/` | Readable skill sources | — |

### Skills
- `dctr-learner-response`
- `dctr-protocol`

`dctr-protocol` is the shared public protocol for all five roles. It deliberately omits the hidden test surface, the rubric and the forbidden exam terms.

### Verbatim vs authored
- **Verbatim:** the policy's one-line role definition, the role id, the pipeline, cohorts, blinding lists, thresholds, critical-failure codes, A09 step order and outcomes.
- **Authored for StarNet:** voice, procedures, record formats. These are marked *"Authored for StarNet from the DCTR policy…"*.

## Upload steps
1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/dctr-learner/`, where it appears as **HERMES — PROFILE DCTR-LEARNER**.
2. **Check the preview.** You should see name DCTR-Learner, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Install the skills.** With this agent active: **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- **This is a template.** A valid trial needs at least six separate learner agents (2 taught, 2 untaught, 2 sham) with fresh memories. Copy this folder once per candidate and rename the heading (e.g. `DCTR-Learner-C`).
- The Data Engineering students are the learners for DE work; this role is for DCTR trials only.
- StarNet cannot enforce DCTR blinding: crew share a station, the Commander dossier, and possibly a filesystem. Isolation is procedural (separate folders, self-reporting of exposure).

## Validation (2026-10-07)
Validated against StarNet `feat/harness-backend@764fcfc8b` in a scratch copy (`/tmp/starnet-scratch`); the repo itself was not modified.
- **Pure engine:** 73/73 checks passed across the five DCTR roles (scan ok, no warnings, no truncation, name/purpose/context caps met, authored label present, every skill guard `allow`, shared `de-curriculum` digest identical).
- **Leak check:** passed. The hidden test surface and forbidden-term material appear only in `dctr-scenario-gen`.
- **Live sidecar:**
  - `/api/harness/detect` listed all five DCTR profiles.
  - `/api/harness/scan` returned ok, with all four docs byte-identical to the files.
  - `/api/skill-exchange/import` then `/install` succeeded for every skill (guard `allow`), and the skills are visible (not withheld).
- **Not exercised:** the browser RECRUIT click.
