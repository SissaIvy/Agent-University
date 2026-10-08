# CodespaceDeveloper (Codespace Developer): StarNet agent context

Packaged as a **Hermes agent home** for StarNet's **Import Agent** flow, plus skill packages. Siblings: `../prof-data-engineering/`, `../dean-librarian/`, `../apprentice-librarian/`, `../computer-data-scientist/`, `../codespace-developer/`; `../faculty-all.zip` bundles all five.

Source material (the `aml` repo): `agents/profiles/codespace_developer/agent.yaml` + `README.md`, `aml` `AGENTS.md` environment notes.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name **CODESPACEDEVELOPER** (from the heading `CodespaceDeveloper`), the purpose line (129 chars), and the persona | 2.1k / 16k |
| `AGENTS.md` | Standing orders | 4.6k / 16k |
| `memories/USER.md` + `memories/MEMORY.md` | Context | 2,105 / 8,000 chars composed |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1`) | 1 |
| `skills-src/` | Readable skill sources (not needed for upload) | — |

There is no `config.yaml`, so the agent uses the station's default model.

### Skills
- `codespace-devcontainer-setup`: requirements → `devcontainer.json` → fresh-build verification → optimization → troubleshooting → docs (authored from the README workflow)

### Verbatim vs authored
There is no system prompt in the University record.
- **Carried verbatim:** role, capabilities, tools (names), learning objectives, README workflow steps, mentorship, tags.
- **Authored for StarNet:** voice, the capability-to-action mapping, the devcontainer procedure. Authored passages are marked *"Authored for StarNet from the structured University profile"* in SOUL.md and AGENTS.md.

## Upload steps

1. In StarNet, open the Recruitment Bay → **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this folder, or
   - copy it to `$HERMES_HOME/profiles/codespace-developer/` (default `~/.hermes/profiles/`; Windows `%LOCALAPPDATA%\hermes\profiles\`). It then appears as **HERMES — PROFILE CODESPACE-DEVELOPER**.
2. **Check the preview.** You should see name CodespaceDeveloper, INSTRUCTIONS present, USER CONTEXT present, a curated MEMORY, model "none found; station default", and only the "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In the dossier, the suggested voice is **composed**.
4. **Install the skills.** With this agent active, open **SKILLS** → skill exchange → **IMPORT EXPORTED PACKAGE** → pick each `skills/*.skill.json` → **INSTALL SKILL**.

## Gaps
- All four declared tools (`codespace_config_manager`, `devcontainer_builder`, `environment_optimizer`, `workspace_analyzer`) have **no implementation** in the repo, and the README's `.ps1` example doesn't exist. The agent is told to do the work directly.
- The `aml` repo has no `.devcontainer/` yet, so there is nothing to maintain, only to create.
- No badge file exists for this agent, unlike the three library agents.
- Its USER.md describes the `aml` dev environment rather than the library, because its job is environments.

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
  - `/api/skill-exchange/import` then `/install` succeeded for all 1 skill(s) (guard `allow`), and they are visible (not withheld) in `/api/agent-skills`.
- **Not exercised:** the browser RECRUIT click. Its purpose, context and name derivations were checked separately.
