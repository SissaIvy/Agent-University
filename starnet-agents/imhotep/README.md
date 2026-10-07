# IMHOTEP: StarNet agent context

IMHOTEP is Agents University's "Architect-Priest of Tasks" and its academic governor. This folder packages it as a **Hermes agent home** for StarNet's **Import Agent** flow, plus four skill packages for StarNet's skill exchange.

Source material: the `aml` repo, mainly `ops/personas/imhotep/`, `ops/tasks/`, `ops/academic/matriculation/`, `agents/faculty/data-engineering/`, and `policies/`.

## What's in the folder

| File | Becomes in StarNet | Size |
|---|---|---|
| `SOUL.md` | Name (`IMHOTEP`, from the first heading), purpose (the first line, 130 chars), and persona (appended under the station's own identity) | 4.7k / 16k |
| `AGENTS.md` | Standing orders (operating manual): schema, overlay rules, A01–A12, gates, role packs, KPIs, role permissions as prose | 11.2k / 16k |
| `memories/USER.md` | Context: "about your Commander" | 1.5k |
| `memories/MEMORY.md` | Context: curated memory (appointments, decisions on record, cohort state, thesis contract) | 3.8k |
| `skills/*.skill.json` | Per-agent skills (`open-agent-skill-package/v1` envelopes) | 4 packages |
| `skills-src/` | Readable source of those packages (not needed for upload) | — |

The combined context doc is 5.3k of the 8k cap.

**No `config.yaml`, on purpose.** Without one, IMHOTEP runs on the station's default model. Pinning a provider you have no key for would break its runs, and any config text containing words like "key" or "auth" triggers StarNet's secrets warning. To pin a model later, set it in IMHOTEP's dossier after import.

### Skills
- `imhotep-task-codification`: generate tasks from text, and validate/fix them with a fixlog. Includes the task schema, sample tasks and overlay rules.
- `imhotep-gate-promotion`: the A06/A07/A08/A09 gates, the University decision gate, hard stops, and the gate report shape.
- `imhotep-task-merge`: merge by A-code without renumbering, using collision suffixes and dependencies.
- `imhotep-academic-validation`: matriculation, pedagogy review, and thesis validation, with the DE-2026-09-29 records as references.

## Upload steps

1. **Import the agent.** In StarNet, open the Recruitment Bay and choose **⇪ IMPORT AGENT**. Then use either option:
   - **PICK FOLDER…** and select this `imhotep/` folder (unzip `imhotep.zip` first if needed), or
   - copy the folder to `$HERMES_HOME/profiles/imhotep/` (default `~/.hermes/profiles/imhotep/`, or `%LOCALAPPDATA%\hermes\profiles\imhotep\` on Windows). It will then appear in the detect list as **HERMES — PROFILE IMHOTEP**.
2. **Check the preview.** You should see name IMHOTEP, the persona excerpt, INSTRUCTIONS present, USER CONTEXT present, MEMORY ≈3760 chars curated, model "none found; station default", and only the standard "keys never transfer" note. Press **▸ RECRUIT**.
3. **Set the voice (optional).** In IMHOTEP's dossier, set the persona voice to **composed** (or **blunt** for sharper gate verdicts).
4. **Install the skills.** With IMHOTEP selected as the active agent, open the **SKILLS** window. In the skill-exchange section, click **IMPORT EXPORTED PACKAGE**, pick a `skills/*.skill.json` file, review it, then click **INSTALL SKILL**. Repeat for all four. They install for whichever agent is active.

## Known limits (by design)

- StarNet cannot enforce IMHOTEP's University role permissions, gates, or autonomy levels. They are carried as written rules, and the persona states that its verdicts are advisory on the station.
- Daily notes and the evidence logs in `.mm-out` are not imported, and there are none here.
- University status (matriculation, cohort state) is context only, per StarNet's University experiment contracts (AU-UCR).

## Validation (2026-10-07)

Validated against StarNet `feat/harness-backend@764fcfc8b` in a scratch copy; the repo itself was not modified.

- **Pure engine (`sidecar/harness-import.js`, `skills/package-format.js`, `skills/exchange.js` + `guard.js`, `frontend/app/agentid.js`): 19 of 19 checks passed.**
  - Detect finds the `HERMES_HOME` profile.
  - The scan returns ok with sources SOUL.md, AGENTS.md, memories/USER.md and memories/MEMORY.md, and no warnings.
  - No field is truncated.
  - Name `IMHOTEP` passes the agent-name check.
  - The purpose is 130 chars, so it is not cut.
  - The context doc is 5,267 chars, under 8,000.
  - All four envelopes round-trip, and the guard verdict is `safe` / `allow` (community trust).
- **Live sidecar HTTP routes** (scratch copy booted with `HERMES_HOME` set to a temp dir):
  - `POST /api/harness/detect` lists "Hermes — profile imhotep".
  - `POST /api/harness/scan` returns ok. Persona, instructions, user context and memory are byte-identical to the files, and there are no warnings.
  - `POST /api/skill-exchange/import` then `/install` returned ok for all four skills (guard `allow`).
  - `GET /api/agent-skills` shows all four installed and not withheld.
- **Not exercised:** the browser RECRUIT click (`confirmImport`). Its purpose, context and name derivations were re-implemented from `frontend/app/marketplace.js` and checked as above.
