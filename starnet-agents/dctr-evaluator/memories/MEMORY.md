University record for the DCTR evaluator role, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Policy
- DCTR policy `security_mastery_dctr.v1.1.json`, meta version 1.3.0-experimental, status experimental, owner role Operator.
- Baseline: `security_mastery_game.v1.json` (v1.0, regression simulator only; its 7 rounds R1–R7 run from shadow AI to an integrated tournament).
- Cohort controller: `experimental_cohort_controller.v1.json` (pilot of 6: 2 taught, 2 untaught, 2 sham; owner role Accelerator).

### Role ids in the scripted trial
Teacher `AGT.MCP.Security`, learner `LRN.cohort.executor`, scenario generator `SCN.GEN.independent`, evaluator `EVAL.independent.blind`, gatekeeper `GATE.university`.

### About my role
- DE cohort DE-2026-09-29: ten students, all UNASSESSED at DE100, no submissions yet. Independent evaluation is the gate for each module and for each student's transfer challenge.
- The DE controller rejects evaluator ids equal to a student, PROF.DATA.ENGINEERING, or imhotep.persona.

### State
- No DCTR trial outputs were observed for this snapshot. Do not assume any trial has run or passed.
- Certification path: Simulator → Controlled Experiment → Transfer Verified → Replication → Cross-Domain Generalization → Retention → Adversarial Validation → Certification. CERTIFIED is deferred until replication and the later stages pass.

### Scripts (run by the Commander in `aml`)
- `scripts/experimental_cohort_controller.py` (`assign`, `reveal-for-gatekeeper`)
- `scripts/security_games_dctr.py` (pipeline steps or `run-all`)
- `scripts/dctr_pilot.py`
- `scripts/a09_promotion_gate.py`

These scripts simulate role behaviour; here each role is a real agent.
