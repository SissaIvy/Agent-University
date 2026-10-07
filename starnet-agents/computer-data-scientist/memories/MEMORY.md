University record for ComputerDataScientist, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Profile
- Source: `agents/profiles/computer_data_scientist/agent.yaml` (no README, no tools declared).
- Badge file `agent_cds.json` shows on duty, busy, error, or offline.

### Where my inputs come from
- Teach packs under `.mm-out/university/teach-packs/*.teach.json`, emitted by the library workflow (`scripts/university_workflow.py teach`).
- Each pack has title, path, track, tags, imports, objectives, exercises. The default exercises are "add a test cell", "swap one model/library variant and compare outputs", and "document failure modes and retries".

### Status
No experiment logs or reproduction results were observed for this snapshot. Do not claim prior results.

### Related University skill standards
The skills matrix (`docs/teachpacks/skills_matrix.v1.csv`) expects rubric level 3 with evidence such as `model_compare`, `metrics_report`, `assumptions_logged` and `eval_run` for modeling and evaluation skills.
