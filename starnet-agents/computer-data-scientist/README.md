# ComputerDataScientist (Computer/Data Scientist): StarNet agent context

Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus skill packages. Siblings: `../prof-data-engineering/`, `../dean-librarian/`, `../apprentice-librarian/`, `../computer-data-scientist/`, `../codespace-developer/`; `../faculty-all.zip` bundles all five.

Source material (the `aml` repo): `agents/profiles/computer_data_scientist/agent.yaml`, the teach-pack format in `scripts/university_workflow.py`, `docs/teachpacks/skills_matrix.v1.csv`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **DATA SCIENTIST** (from the heading `DATA SCIENTIST`), the purpose line (136 chars), and the persona | 1.9k / 16k |
| `AGENTS.md` | Standing orders | 3.8k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 2,411 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 2 |
| `skills-src/` | Readable skill sources (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model.

### Skills
- `teach-pack-reproduction`: deterministic reproduction, one-variant comparisons, experiment-log shape (authored)
- `university-library-workflow`: where teach packs come from and their format (**shared**)

### Verbatim vs authored
There is no system prompt in the University record.
- **Carried verbatim:** role, capabilities, learning objectives, mentorship, tags.
- **Authored for StarNet:** voice, experiment rules, the reproduction procedure and the experiment-log shape. Authored passages are marked *"Authored for StarNet from the structured University profile"* in SOUL.md and AGENTS.md.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/computer-data-scientist/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE COMPUTER-DATA-SCIENTIST**.
2. **Check the preview.** You should see name DATA SCIENTIST, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With this agent active, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- `ComputerDataScientist` is 21 chars, over the cap, so the display name is **DATA SCIENTIST**.
- The profile declares **no tools**, and has no README, system prompt or voice. All procedure is authored (labelled).
- No experiment logs exist in the repo, so there is no prior work to carry.

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
  - `/api/skill-exchange/import` then `/install` succeeded for all 2 skill(s) (guard `allow`), and they are visible (not withheld) in `/api/agent-skills`.
- **Not exercised:** the browser RECRUIT click. Its purpose, context and name derivations were checked separately.
