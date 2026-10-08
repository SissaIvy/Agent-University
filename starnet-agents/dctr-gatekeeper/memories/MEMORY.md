University record for the DCTR gatekeeper role, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Policy
- DCTR policy `security_mastery_dctr.v1.1.json`, meta version 1.3.0-experimental, status experimental, owner role Operator.
- Baseline: `security_mastery_game.v1.json` (v1.0, regression simulator only; its 7 rounds R1–R7 run from shadow AI to an integrated tournament).
- Cohort controller: `experimental_cohort_controller.v1.json` (pilot of 6: 2 taught, 2 untaught, 2 sham; owner role Accelerator).

### Role ids in the scripted trial
Teacher `AGT.MCP.Security`, learner `LRN.cohort.executor`, scenario generator `SCN.GEN.independent`, evaluator `EVAL.independent.blind`, gatekeeper `GATE.university`.

### About my role
- Scripted equivalent: `python scripts/security_games_dctr.py decision-gate`, which calls `scripts/a09_promotion_gate.py` (`evaluate_a09_gate`).
- No DCTR trial results were observed for this snapshot. The policy path to certification is still at an early stage.

### State
- No DCTR trial outputs were observed for this snapshot. Do not assume any trial has run or passed.
- Certification path: Simulator → Controlled Experiment → Transfer Verified → Replication → Cross-Domain Generalization → Retention → Adversarial Validation → Certification. CERTIFIED is deferred until replication and the later stages pass.

### Scripts (run by the Commander in `aml`)
- `scripts/experimental_cohort_controller.py` (`assign`, `reveal-for-gatekeeper`)
- `scripts/security_games_dctr.py` (pipeline steps or `run-all`)
- `scripts/dctr_pilot.py`
- `scripts/a09_promotion_gate.py`

These scripts simulate role behaviour; here each role is a real agent.
