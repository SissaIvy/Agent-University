# Production deployment runbook: Agents University → StarNet

This runbook follows the approved order: **IMHOTEP first** (the governance authority), then the **DCTR roles** (the governance mechanism), then the **Data Engineering cohort** (governed instruction). Every package here was validated against a scratch StarNet (`feat/harness-backend@764fcfc8b`). This runbook is the **production** validation: treat nothing as proven on your station until its receipt is captured.

Packages live next to this file: `imhotep/`, `dctr-*/`, `prof-data-engineering/`, the four staff folders, and `de-stu-001…010/`. Each has a zip and a README with its own upload steps.

## Before you start
- Note your StarNet version (Settings → About) and that the station is running.
- Choose a receipts folder. Suggested: `.mm-out/starnet-deploy/` in your `aml` checkout (gitignored, append-only by convention).
- **Keys never transfer.** Make sure the station's default model works before recruiting.

## Phase 1: IMHOTEP
1. **Import:** Recruitment Bay → ⇪ IMPORT AGENT → PICK FOLDER → `imhotep/`.
   - The preview should show: name IMHOTEP; INSTRUCTIONS present; USER CONTEXT present; MEMORY ≈3,760 chars curated; model "station default"; only the keys-never-transfer note.
   - Screenshot the preview.
2. **Recruit:** press ▸ RECRUIT. Check that IMHOTEP appears in the crew and its dossier shows the purpose line ("Architect-Priest of Tasks: …").
3. **Skills:** with IMHOTEP active: SKILLS → IMPORT EXPORTED PACKAGE → install all four from `imhotep/skills/`. Each should install without a "withheld" badge.
4. **Startup check:** ask *"Who are you, and what are you not allowed to do?"* Expected: it names itself IMHOTEP and the Architect-Priest role, lists the non-goals (it does not do the owner's work, and does not choose at A09 without evidence), and says its gates are advisory on this station.
5. **Memory check:** ask *"What decisions do you have on record for cohort DE-2026-09-29?"* Expected:
   - the matriculation (M01–M08 passed, AWAITING_STUDENT_RUNS);
   - the pedagogy review APPROVED_WITH_CONTROLS, with effectiveness UNPROVEN;
   - a statement that no native IMHOTEP service was observed.
6. **Governance workflow:** paste a short meeting note, for example *"Ana will draft the data contract for the orders feed by Friday; CI schema checks are blocked on the runner upgrade."* Ask IMHOTEP to codify it with the #SISSA role pack, then validate the result. Expected:
   - an A-coded `{meta, tasks}` JSON that satisfies the schema, with `source_reference` and `memory_correlation`;
   - the blocked task carries dependencies and risk notes (overlay rule);
   - the due-within-3-days rule applied if relevant;
   - a `meta.fixlog` on validate.
7. **Receipt:** write the receipt below and save the codified JSON next to it.

## Phase 2: DCTR roles
1. Import and recruit `dctr-evaluator`, `dctr-gatekeeper`, `dctr-teacher` and `dctr-scenario-gen`, then install each agent's own skills only.
   - **Never install `dctr-hidden-scenario` on any agent except DCTR-ScenarioGen.**
2. **Learners:** copy `dctr-learner/` once per candidate, at least six for a valid trial (2 taught, 2 untaught, 2 sham). Rename each copy's `# DCTR-Learner` heading (e.g. `DCTR-Learner-A`, at most 18 characters), then import, recruit and install the skills for each.
3. **Isolation:** StarNet cannot enforce DCTR blinding. Keep each role's files in its own folder. For certification-grade trials, run the ScenarioGen and Evaluator on a separate station or workspace.
4. **Smoke checks:**
   - Ask the evaluator for its evaluator id. Expected: `EVAL.independent.blind`.
   - Ask the gatekeeper what a single passing trial yields. Expected: HOLD, awaiting replication.
   - Ask the teacher whether it may see the exam. Expected: no, and it would report `hidden_test_leakage`.
5. Write a receipt per agent.

## Phase 3: Data Engineering cohort
1. Import and recruit `prof-data-engineering`, then the staff folders as needed, then `de-stu-001…010`. Install the skills: 4 for the professor, 3 per student.
   - Shortcut: copy all ten student folders into `$HERMES_HOME/profiles/`, and they appear in the detect list together. Each still needs its own RECRUIT and skill installs.
2. **Issue DE100** in your `aml` checkout:
   - `python scripts/data_engineering_cohort.py validate`
   - `python scripts/data_engineering_cohort.py matriculation-status`
   - `python scripts/data_engineering_cohort.py issue --module DE100`
3. Hand each student its assignment packet (`.mm-out/…/DE-STU-0NN/DE100/assignment_packet.json`) on the station.
4. Write receipts.

## Phase 4: Governed workflow validation (one student end-to-end)
1. **Learning:** DE-STU-001 produces `source_inventory` and `data_contract` plus a `submission_manifest.json`. Record it with `ingest --student DE-STU-001 --module DE100 --artifact <file>`.
2. **Evaluation:** DCTR-Evaluator writes the evaluation JSON (evaluator id `EVAL.independent.blind`). Record it with `evaluate --student DE-STU-001 --module DE100 --result <file>`. The controller must accept the evaluator id.
3. **Promotion:** run `status`, which should show DE-STU-001 at 1/10 modules if passed. No promotion happens without evidence.
4. **Governance:** ask IMHOTEP to codify the DE100 run as tasks and produce an A06/A09 gate report from the recorded evidence. Expected: HOLD or GO with the evidence cited, never a decision without the artifacts.

## Receipt template (one per agent and phase)
```json
{
  "receipt_id": "STARNET-DEPLOY-<agent>-<YYYYMMDD>-01",
  "agent": "IMHOTEP",
  "package": "docs/starnet-agents/imhotep.zip",
  "package_sha256": "<sha256 of the zip you imported>",
  "starnet_version": "<from Settings → About>",
  "imported_at": "<ISO timestamp>",
  "preview": {"name": "IMHOTEP", "instructions": true, "user_context": true, "memory_chars": 3760, "model": "station default", "warnings": ["keys never transfer"]},
  "recruited": true,
  "skills_installed": [{"slug": "imhotep-task-codification", "withheld": false}],
  "startup_check": "pass | fail — <one line>",
  "memory_check": "pass | fail — <one line>",
  "workflow_check": "pass | fail — <artifact path>",
  "issues": [],
  "operator": "<you>",
  "scratch_validation_ref": "README.md § Validation (scratch StarNet 764fcfc8b)"
}
```

## Known limits to keep in mind
- **Gates are advisory.** IMHOTEP's gates and permissions and the DCTR blinding are carried as rules; StarNet enforces none of them.
- **The `aml` controllers are the system of record** for cohort and trial evidence. StarNet holds the working agents.
- **Skill installs are manual and per agent:**
  - 4 for IMHOTEP;
  - 12 for the DCTR roles, with learners adding 2 each;
  - 11 for the faculty;
  - 30 for the students.
