---
name: DCTR A09 Gate
slug: dctr-a09-gate
description: Gatekeeper procedure for the DCTR A09 certification gate - deterministic step sequence, thresholds, critical-failure veto and the CERTIFIED / HOLD / REJECTED / ROLLED_BACK decision record.
category: Governance
version: 1.3.0-experimental
author: Agents University (authored for StarNet from the DCTR policies and scripts)
---

The independent A09 certification decision for DCTR, mirroring `scripts/a09_promotion_gate.py` (`evaluate_a09_gate`). The authorized gatekeeper id is in your standing orders.

## Inputs (and only these)
Anonymized scores from the evaluator, control deltas, the auditor (access-isolation) report, the evidence bundle and its hash, the policy version. Treatments are revealed to you only after blind scoring.

## Pre-checks
1. **Rollback trigger active?** Then the decision is **ROLLED_BACK** and certification authority is revoked.
2. **Gate actor not the authorized gatekeeper?** Then the decision is **REJECTED**.

## Deterministic sequence: stop at the first failing step, which sets the outcome
| # | Step | Outcome if it fails |
|---|---|---|
| 1 | `evidence_valid` | HOLD |
| 2 | `experimental_design_valid` | HOLD |
| 3 | `sample_requirements_satisfied` | HOLD |
| 4 | `treatment_control_criteria_satisfied` | REJECTED |
| 5 | `pre_post_gain_satisfied` | REJECTED |
| 6 | `hidden_transfer_satisfied` | REJECTED |
| 7 | `retention_satisfied` | HOLD |
| 8 | `adversarial_requirements_satisfied` | REJECTED |
| 9 | `critical_failure_veto_clear` | REJECTED (or HOLD if policy says) |
| 10 | `drift_acceptable` | HOLD |
| 11 | `maturity_threshold_satisfied` | HOLD |

All pass gives **CERTIFIED**, but by policy CERTIFIED is **deferred** until replication, cross-domain generalization, retention and adversarial validation have passed across multiple trials. Until then the honest outcome for a single passing trial is HOLD, with "awaiting replication".

## Thresholds (policy v1.3.0-experimental)
- Hidden scenario score ≥ 0.9; pre-test improvement ≥ 0.2; pre-test equivalence Δ ≤ 0.1.
- Control advantage ≥ 0.15; retention control advantage ≥ 0.15; retention ≥ 0.85.
- At least 2 receivers and 2 domains; critical errors ≤ 0.
- Significance α ≤ 0.1; effect size d ≥ 0.8; maturity ≥ 70.
- Samples: min_treatment_n=2, min_control_n=2, min_sham_n=2, min_receivers=2, min_domains=2.
- Maturity weights: transfer_significance 0.25, improvement_significance 0.2, retention_significance 0.25, adversarial_robustness 0.15, evidence_completeness 0.15.

## Critical failure veto
- Any REJECT code: hidden_test_leakage, evidence_tampering, self_certification_attempt, treatment_control_leakage, duplicate_evidence_detected, replayed_successful_experiment, catastrophic_transfer_failure, evaluator_contamination, invalid_experimental_isolation.
- HOLD codes: missing_retention_evidence, provenance_verification_failed, sample_insufficient.
- No score compensates a critical failure.

## Decision record
    { "decision": "HOLD", "policy_version": "1.3.0-experimental", "evidence_bundle_hash": "…",
      "failed_step": "retention_satisfied", "steps": [{"step": "…", "passed": true, "failure_state": "…", "detail": "…"}],
      "rationale": "…", "gate_actor": "<your gatekeeper id>", "decided_at": "…" }

Save it, hash it, and hand it to the Commander. The scripted equivalent is `python scripts/security_games_dctr.py decision-gate`.

## Never
- Re-score responses or adjust thresholds after seeing results.
- Certify on a single trial.
- Decide Data Engineering thesis validation, which is IMHOTEP's authority, or DE module passage, which is the evaluator's.
