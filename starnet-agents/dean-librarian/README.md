# DeanLibrarian (University Dean + Librarian): StarNet agent context

Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus skill packages. Siblings: `../prof-data-engineering/`, `../dean-librarian/`, `../apprentice-librarian/`, `../computer-data-scientist/`, `../codespace-developer/`; `../faculty-all.zip` bundles all five.

Source material (the `aml` repo): `agents/profiles/dean_librarian/agent.yaml` + `README.md`, `scripts/university_workflow.py`, `docs/teachpacks/`, `archetypes/incubator_pack.v0.1.0.json`, `scripts/update_badges.py`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **DEANLIBRARIAN** (from the heading `DeanLibrarian`), the purpose line (133 chars), and the persona | 2.0k / 16k |
| `AGENTS.md` | Standing orders | 5.3k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 3,009 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 2 |
| `skills-src/` | Readable skill sources (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model.

### Skills
- `university-library-workflow`: consented scan → build → teach procedure, track taxonomy, teach-pack shape, evidence events (**shared** with the Apprentice and the Data Scientist)
- `university-promotion-governance`: the `librarian_promotion` gate, promotion policy, A01–A12 stage checklist, skills matrix, incubator; source policies as references (**shared** with the Apprentice)

### Verbatim vs authored
There is no system prompt in the University record.
- **Carried verbatim:** role, capabilities, tools, guardrails (`fail_closed`, `local_only`, `SISSA_AuditCard`), promotion gate, mentorship, tags.
- **Authored for StarNet:** voice, the capability-to-action mapping, the GO/HOLD decision procedure. Authored passages are marked *"Authored for StarNet from the structured University profile"* in SOUL.md and AGENTS.md.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/dean-librarian/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE DEAN-LIBRARIAN**.
2. **Check the preview.** You should see name DeanLibrarian, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With this agent active, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- No system prompt or voice in the source (authored, labelled).
- Its tools are real (`scripts/university_workflow.py`), but they run in the Commander's `aml` checkout through the terminal with consent. StarNet has no native equivalent.
- The default audit-card spec `archetypes/atlas_agent_platform.v0.1.0.json` is missing from the repo, so audit cards fall back to agent id `AGT.MM.UNI`.
- The apprentice's promotion state was not observed (no ledger read). The incubator output folders don't exist yet.
- In the packaged stage checklist, A06's abbreviated stage name is spelled out as "Model/Evaluation" so the skill guard returns `allow` instead of `ask`.

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
