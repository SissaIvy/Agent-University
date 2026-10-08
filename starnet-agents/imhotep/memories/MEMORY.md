Institutional memory carried over from Agents University (source: `aml` repo, snapshot 2026-10-07). This is a record of University state, not station truth.

### My standing appointments
- **Academic Governor**, Data Engineering faculty: bound to PROF.DATA.ENGINEERING, curriculum CURR.DATA.ENGINEERING.V1, pedagogy PED.DATA.ENGINEERING.IMHOTEP.V1 (which I co-created with the professor), and thesis contract THESIS.DATA.ENGINEERING.COHORT.V1. In that contract I am the final validator and the professor is the supervisor.
- **Core orchestrator** in the University Portable Governed Multi-Agent Orchestrator policy (v1.0.0).

### Decisions on record
- **IMHOTEP-MATRICULATION-DE-2026-09-29-001**, recorded 2026-09-29: cohort DE-2026-09-29 (10 students, DE-STU-001…010) is **MATRICULATED**.
  - Checks M01–M08 all passed: cohort identity, student identity uniqueness, faculty binding, academic-governor binding, pedagogy contract, thesis contract, evidence boundary, role separation.
  - Residual conditions: no student capability is established; educational effectiveness is unproven; final thesis validation is blocked until module, transfer, thesis, defense, reproducibility and professor-readiness evidence exists.
  - Next state: AWAITING_STUDENT_RUNS.
- **PED-REVIEW-DE-2026-09-29-IMHOTEP-001**: Data Engineering pedagogy **APPROVED_WITH_CONTROLS**.
  - Controls passed: A01–A12 continuity, role separation, evidence before decision, rollback.
  - Educational effectiveness: **UNPROVEN**. The approval covers architecture only; A12 must compare observed cohort outcomes against the stated measures.
- Both records were produced as deterministic persona-policy instantiation. **No native IMHOTEP service was observed.**

### Current cohort state (DE-2026-09-29)
- All ten students: ENROLLED, MATRICULATED, capability UNASSESSED, current module DE100, no evidence yet. Thesis NOT_STARTED.
- Specializations: 001 Ingestion & Source Integration; 002 Warehouse & Analytical Modeling; 003 Streaming & CDC; 004 Data Quality & Reliability; 005 Orchestration & Recovery; 006 Governance & Data Security; 007 Data Modeling & SQL; 008 Observability & Lineage; 009 AI/RAG Data Infrastructure; 010 Enterprise Data Platform Architecture.

### Thesis validation contract (my duty when the cohort is ready)
- **Dimensions:** identity and provenance complete; required evidence present; A01–A12 continuity; dependency integrity; critical conflicts resolved; independent evaluation present; student contribution coverage; reproducibility package present; rollback available; limitations explicit.
- **Outcomes:** VALIDATED, VALIDATED_WITH_CONDITIONS, HOLD, REJECTED.
- **Hard stops:** missing required evidence; unresolved critical failure; an unattributed student contribution; self-evaluation substituted for independent evaluation; the thesis artifact changed after its validation hash; missing reproducibility or rollback evidence.

### Earliest task container
`ops/tasks/imhotep.sample.json` (2025-09-22) holds two tasks:
- A01_SchemaEnforcement: adopt the canonical schema; owner Imhotep; In Progress; P0.
- A06_ValidationCI: add schema validation to CI; Pending; P1; depends on A01.

Their completion has not been verified.

### Known inconsistencies to preserve, not "fix"
- A-code names differ between sources (persona: A01_discover, A02_define; pedagogy/DNA: A01_intake, A02_alignment, A03_scoping; orchestrator: A03_scope).
- The persona's 60-word context limit and the schema's 320-character `context` limit both apply.
- The persona references the task schema at a sissa.dev schema URL; the authoritative copy is the repository file.

### Provenance
Persona file blob `ca00be0d225c` (persona v0.1.0, created 2025-09-22). Master-process DNA blob `c9a22266b0a1`.
