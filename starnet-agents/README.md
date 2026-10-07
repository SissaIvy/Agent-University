# Agents University: StarNet agent contexts

These are ready-to-import agent contexts for StarNet, built from the Agents University material in `mrrobot787/aml`. Each folder is a **Hermes agent home** for StarNet's **Import Agent** flow (Recruitment Bay → ⇪ IMPORT AGENT → PICK FOLDER), with skill packages under `skills/` (`open-agent-skill-package/v1`). Each folder's own `README.md` has upload steps, gaps, and validation results.

Start with [`production-deployment-runbook.md`](production-deployment-runbook.md). It covers IMHOTEP first, then the DCTR roles, then the Data Engineering cohort, with a receipt template.

| Group | Folders | StarNet names |
|---|---|---|
| Governance | `imhotep/` | IMHOTEP |
| DCTR roles | `dctr-teacher/`, `dctr-learner/` (template: one copy per candidate), `dctr-evaluator/`, `dctr-gatekeeper/`, `dctr-scenario-gen/` | DCTR-Teacher, DCTR-Learner, DCTR-Evaluator, DCTR-Gatekeeper, DCTR-ScenarioGen |
| Faculty | `prof-data-engineering/` | PROF DATA ENG |
| Library staff | `dean-librarian/`, `apprentice-librarian/`, `computer-data-scientist/`, `codespace-developer/` | DeanLibrarian, APPRENTICE LIB, DATA SCIENTIST, CodespaceDeveloper |
| DE cohort DE-2026-09-29 | `de-stu-001/` … `de-stu-010/` | DE-STU-001 … DE-STU-010 |

**Quick local install.** Copy the folders into `~/.hermes/profiles/` (Windows: `%LOCALAPPDATA%\hermes\profiles\`). They then all appear in Import Agent's detect list. Each one still needs its own RECRUIT, and its skills are installed per agent via SKILLS → IMPORT EXPORTED PACKAGE.

**Keep sealed material sealed.** Install `dctr-scenario-gen/skills/dctr-hidden-scenario.skill.json` on DCTR-ScenarioGen only. It contains the hidden exam material.

**Validation.** Every package was validated on 2026-10-07 against StarNet `feat/harness-backend@764fcfc8b` in a scratch copy:
- the pure import engine;
- a live sidecar run: detect, scan with byte-identical docs, and skill import/install with guard `allow`.

The browser RECRUIT click was not exercised, so the runbook is the production check.

`skills-src/` folders hold the readable sources of each skill package. They are not needed for upload.
