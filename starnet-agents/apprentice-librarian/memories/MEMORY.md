University record for ApprenticeLibrarian, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Profile
- Source: `agents/profiles/apprentice_librarian/agent.yaml` (no README).
- Badge file `agent_apprentice.json` shows on duty, busy, error, or offline.

### Promotion
- Gate `librarian_promotion`, administered by the Dean: teach_packs_emitted ≥ 50, report_built, audit_present.
- Current progress: **not observed** (no ledger read for this snapshot). Start by reading `.mm-out/university/evidence.jsonl` and counting `teach_packs_emitted` events before claiming any progress.

### Library workflow facts
- Entry point: `scripts/university_workflow.py` (`scan` | `build` | `teach` | `all`); wrapper `scripts/university.ps1`.
- Outputs go to `.mm-out/university/`.
- Teach-pack fields: title, path, track, tags, imports, objectives, exercises. The generated objectives and exercises are generic templates, and improving them is my job.
- The audit-card atlas spec is missing from the repo, so audit cards fall back to agent id `AGT.MM.UNI`.
