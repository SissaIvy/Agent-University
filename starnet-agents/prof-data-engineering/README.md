# PROF.DATA.ENGINEERING (Professor_Data_Engineering_v1.0): StarNet agent context

Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus skill packages. Siblings: `../prof-data-engineering/`, `../dean-librarian/`, `../apprentice-librarian/`, `../computer-data-scientist/`, `../codespace-developer/`; `../faculty-all.zip` bundles all five.

Source material (the `aml` repo): `agents/faculty/data-engineering/professor.json`, `pedagogy.v1.json`, `curriculum.v1.json`, `thesis_contract.v1.json`, `pedagogy_review.imhotep.v1.json`, `agents/cohorts/DE-2026-09-29/`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **PROF DATA ENG** (from the heading `PROF DATA ENG`), the purpose line (134 chars), and the persona | 3.0k / 16k |
| `AGENTS.md` | Standing orders | 6.0k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 2,836 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 4 |
| `skills-src/` | Readable skill sources (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model.

### Skills
- `de-cohort-thesis`: the thesis contract, 15 sections, derived ownership map (**shared**)
- `de-curriculum`: the ten modules, evaluation dimensions, critical-failure and completion rules (**shared**, byte-identical to the students' copy)
- `de-module-work`: the student module procedure and submission manifest, so the professor knows exactly what students follow (**shared**)
- `de-professor-teaching`: the professor's own procedure: assignment packets after matriculation, teaching, formative feedback, routing to independent evaluation, thesis supervision, the readiness recommendation template, A12 input (authored)

### Verbatim vs authored
There is no system prompt in the University record.
- **Carried verbatim:** mission, operating principles, responsibilities, prohibited actions, evidence contract, role separation, instructional methods, effectiveness measures, rollback.
- **Authored for StarNet:** voice and teaching style, the teaching loop procedure, the readiness-recommendation format. Authored passages are marked *"Authored for StarNet from the structured University profile"* in SOUL.md and AGENTS.md.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/prof-data-engineering/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE PROF-DATA-ENGINEERING**.
2. **Check the preview.** You should see name PROF DATA ENG, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With this agent active, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- The University id `PROF.DATA.ENGINEERING` (21 chars) exceeds StarNet's 18-char name cap, so the display name is **PROF DATA ENG**; the full id is in the persona.
- No system prompt or voice in the source; voice and teaching procedure are authored (labelled).
- No readiness-recommendation schema exists in the repo; the JSON shape in `de-professor-teaching` is authored.
- The cohort has no student evidence yet, so the professor has nothing to give feedback on until the Commander runs DE100.

## Fix (2026-10-07)
The readiness recommendation is now strictly `READY` or `NOT_READY`, with caveats in separate `conditions` / `open_risks` fields. The cohort controller's `thesis-ingest` rejects any other value; an earlier version of this package allowed `READY_WITH_CONDITIONS`. Only `AGENTS.md` and the `de-professor-teaching` skill changed. Re-validated: pure engine 19/19, and the live sidecar scan and all 4 installs passed.

## Validation (2026-10-07)

Validated against StarNet `feat/harness-backend@764fcfc8b` in a scratch copy (`/tmp/starnet-scratch`); the repo itself was not modified.

- **Pure engine:** 74/74 checks passed across the five faculty agents.
  - The scan returns ok with 4 sources, no warnings, and nothing truncated.
  - The name passes the agent-name check and is ≤18 chars.
  - The purpose is ≤140 chars, and the context is ≤8,000 chars.
  - The authored-content label is present.
  - Every skill passes the guard as `allow`.
  - The professor's three DE skills have digests identical to the students' copies.
- **Live sidecar:**
  - `/api/harness/detect` listed all 5 faculty profiles.
  - `/api/harness/scan` for this agent returned ok, with all four docs byte-identical to the files.
  - `/api/skill-exchange/import` then `/install` succeeded for all 4 skill(s) (guard `allow`), and they are visible (not withheld) in `/api/agent-skills`.
- **Not exercised:** the browser RECRUIT click. Its purpose, context and name derivations were checked separately.
