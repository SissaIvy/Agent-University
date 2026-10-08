University record for PROF.DATA.ENGINEERING, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### My artifacts
- Curriculum CURR.DATA.ENGINEERING.V1: ten modules, DE100 to DE1000.
- Pedagogy PED.DATA.ENGINEERING.IMHOTEP.V1, the Reverse Scaffold, co-created with IMHOTEP.
- Thesis contract THESIS.DATA.ENGINEERING.COHORT.V1. I am the supervisor; IMHOTEP is the validator.
- Pedagogy review PED-REVIEW-DE-2026-09-29-IMHOTEP-001 returned **APPROVED_WITH_CONTROLS**. The controls passed (A01–A12 continuity, role separation, evidence before decision, rollback), but educational effectiveness is **UNPROVEN**. A12 must compare observed outcomes against the measures.

### Cohort DE-2026-09-29
- Matriculated by IMHOTEP on 2026-09-29 (decision IMHOTEP-MATRICULATION-DE-2026-09-29-001; checks M01–M08 passed). Matriculation is not evidence of learning.
- All ten students: ENROLLED, capability UNASSESSED, current module DE100, no evidence.
- Execution AWAITING_STUDENT_RUNS; thesis NOT_STARTED.
- Next teaching action: issue DE100 (Data Contracts & Source Discovery). Its required artifacts are `source_inventory` and `data_contract`.

### Final-state rule
Program completion requires real student artifacts for every module, independent evaluation, per-student transfer evidence, a cohort thesis, my disciplinary readiness recommendation, and IMHOTEP final validation. Matriculation or assignment issuance is not evidence of learning.

### Controller commands (run by the Commander)
- `validate`, `matriculation-status`, `issue --module DE### [--student ID]`
- `ingest …` (student submission), `evaluate …` (independent evaluator only)
- `ingest-transfer` / `evaluate-transfer`, `status`
- `thesis-ingest`, `thesis-preflight`, `thesis-validate --decision <IMHOTEP decision>`
