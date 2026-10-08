---
name: DCTR Protocol
slug: dctr-protocol
description: Public protocol for Agents University DCTR trials (Double-blind Cross-domain Transfer and Retention) - pipeline, roles, cohorts, blinding rules, critical failure codes and evidence chain. Contains no hidden exam material.
category: Governance
version: 1.3.0-experimental
author: Agents University (Operator; authored for StarNet from policies/security_mastery_dctr.v1.1.json)
---

DCTR answers one question: **did teaching measurably change an agent's ability to solve unfamiliar problems?** Certification is decided only from reproducible evidence and policy gates. This public skill deliberately omits the hidden test surface, the rubric and the forbidden exam terms; only the scenario generator holds those.

## Status
- Experimental. The v1.0 security mastery game is a regression/simulator baseline only; do not treat its scores or badges as proof of mastery.
- If DCTR becomes unstable or contaminated, operational decisions revert to the v1.0 regression baseline while the experimental layer is fixed. Failed attempts are preserved append-only.

## Roles (verbatim)
- **teacher**: delivers teach pack only; never builds the exam
- **learner**: produces responses only; never sees rubric or hidden scenario in advance
- **evaluator**: scores anonymized Candidate-* responses; never constructs the exam; never sees treatment labels
- **gatekeeper**: issues CERTIFIED/HOLD/REJECTED/ROLLED_BACK from evaluator + auditor outputs only
- **scenario_generator**: builds hidden exams; isolated from teacher, learner, and evaluator

## Cohorts
- `taught_receiver` receives: teach_pack
- `untaught_control` receives: none
- `sham_control` receives: plausible_irrelevant_lesson

Pilot size 6: 2 taught, 2 untaught, 2 sham. Candidates are anonymized as `Candidate-A`, `Candidate-B`, and so on.

## Pipeline
cohort_assign → snapshot → blind_pretest → teach → access_isolation → hidden_transfer_test → blind_evaluation → control_comparison → adversarial_mutation → delayed_retention → decision_gate

The public concept is `trust_boundary_reasoning`, taught via the surface `mcp_tool_descriptor_governance`. The hidden transfer test uses a materially different, unseen domain.

## Blinding
- **Evaluator sees:** candidate_id, response_hash, response_text.
- **Evaluator must not see:** cohort, treatment, teach_pack, agent_specialty.
- **Gatekeeper sees:** anonymized_scores, control_deltas, auditor_report.
- Treatments are revealed to the gatekeeper only after blind scoring.

## Critical failure codes
- **REJECT:** hidden_test_leakage, evidence_tampering, self_certification_attempt, treatment_control_leakage, duplicate_evidence_detected, replayed_successful_experiment, catastrophic_transfer_failure, evaluator_contamination, invalid_experimental_isolation.
- **HOLD:** missing_retention_evidence, provenance_verification_failed, sample_insufficient.

Critical failures cannot be compensated by other scores.

## Gate outcomes
CERTIFIED, HOLD, REJECTED, ROLLED_BACK. CERTIFIED is deferred until replication, cross-domain generalization, retention and adversarial validation have passed across multiple trials.

## Path to certification
Simulator → Controlled Experiment → Transfer Verified → Replication → Cross-Domain Generalization → Retention → Adversarial Validation → Certification

## Evidence chain fields (every trial record)
teacher, teach_pack_hash, receiver, candidate_id, treatment_hash, curriculum_hash, pretest_hash, hidden_scenario_hash, response_hash, evaluator_id, rubric_version, baseline_score, post_score, control_delta, retention_score, critical_error_count, gate_result.

Provenance hashes use compact JSON with sorted keys.

## Where it runs
In the Commander's `aml` checkout, with consent:
- `python scripts/experimental_cohort_controller.py assign` (blinded cohort assignment)
- `reveal-for-gatekeeper` (after blind scoring only)
- `python scripts/security_games_dctr.py <step>`, where the steps are snapshot, blind-pretest, teach, access-isolation, hidden-transfer-test, blind-evaluation, control-comparison, adversarial-mutation, delayed-retention, benchmark-suite, decision-gate, or run-all
- `python scripts/dctr_pilot.py` (phase-1 pilot)

Outputs go under `.mm-out/security-games-dctr/` and `.mm-out/accelerator-experiments/`. The script simulates role behaviour; on this station each role is a real agent and follows its own skill.
