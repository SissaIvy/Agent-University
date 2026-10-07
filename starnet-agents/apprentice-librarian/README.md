# ApprenticeLibrarian (Apprentice Librarian): StarNet agent context

Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus skill packages. Siblings: `../prof-data-engineering/`, `../dean-librarian/`, `../apprentice-librarian/`, `../computer-data-scientist/`, `../codespace-developer/`; `../faculty-all.zip` bundles all five.

Source material (the `aml` repo): `agents/profiles/apprentice_librarian/agent.yaml`, `scripts/university_workflow.py`, `docs/teachpacks/`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **APPRENTICE LIB** (from the heading `APPRENTICE LIB`), the purpose line (120 chars), and the persona | 1.8k / 16k |
| `AGENTS.md` | Standing orders | 4.7k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 2,427 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 2 |
| `skills-src/` | Readable skill sources (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model.

### Skills
- `university-library-workflow`: scan/build/teach procedure, tracks, teach-pack shape (**shared**)
- `university-promotion-governance`: its own `librarian_promotion` gate and the promotion policy (**shared** with the Dean)

### Verbatim vs authored
There is no system prompt in the University record.
- **Carried verbatim:** role, capabilities, tools, learning objectives, mentorship, tags, the promotion gate it works toward.
- **Authored for StarNet:** voice, the capability-to-action mapping, working rules, the teach-pack quality bar. Authored passages are marked *"Authored for StarNet from the structured University profile"* in SOUL.md and AGENTS.md.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/apprentice-librarian/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE APPRENTICE-LIBRARIAN**.
2. **Check the preview.** You should see name APPRENTICE LIB, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With this agent active, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- `ApprenticeLibrarian` is 19 chars, over the 18-char cap, so the display name is **APPRENTICE LIB**.
- No README, system prompt or voice in the source (authored, labelled).
- Promotion progress (N of 50 teach packs) was not observed; the agent is told to count it from the evidence ledger.
- The same tooling caveats as the Dean apply (terminal in the `aml` checkout; atlas spec missing).

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
