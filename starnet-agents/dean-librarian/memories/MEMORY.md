University record for DeanLibrarian, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Profile
- Source: `agents/profiles/dean_librarian/agent.yaml` and `README.md`.
- Badges: `update_badges.py` publishes my status as on duty, busy, error, or offline (badge file `agent_dean.json`).

### Library workflow facts
- Entry point: `scripts/university_workflow.py` (`scan` | `build` | `teach` | `all`), with the PowerShell wrapper `scripts/university.ps1`.
- Outputs go to `.mm-out/university/`: `evidence.jsonl`, `notebooks_index.jsonl`, `catalog.json`, the report, and `teach-packs/*.teach.json`.
- The default audit-card spec `archetypes/atlas_agent_platform.v0.1.0.json` is **absent** from the repo, so audit cards fall back to agent id `AGT.MM.UNI`. Treat that as a known gap.
- README usage example: teach over a GitHub folder with `--max-files 5000`, including `**/*.ipynb,**/*.py` and excluding venv, node_modules and checkpoints.

### Promotion and incubator
- My apprentice's gate `librarian_promotion`: teach_packs_emitted ≥ 50, report_built, audit_present.
- Status: **not observed**. No ledger was read for this snapshot, so do not assume it has passed.
- The incubator's output folders (`agents/specialties`, `agents/pupils`) do not exist yet, so no incubator run has produced output.

### Teach-pack governance
`docs/teachpacks/`: `promotion_policy.v1.json`, `stage_checklist.v1.csv` (A01–A12 artifacts and exit gates), `skills_matrix.v1.csv` (9 skills, rubric level 3), and a GitHub-rulesets ops teach pack. The validator `scripts/teachpacks_validate.py` writes a promotion report under `.mm-out/governance/`.
