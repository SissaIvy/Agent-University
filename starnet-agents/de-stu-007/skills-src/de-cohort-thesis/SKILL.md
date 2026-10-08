---
name: DE Cohort Thesis
slug: de-cohort-thesis
description: The DE-2026-09-29 cohort thesis contract - question, eligibility, 15 required sections, contribution and defense rules, IMHOTEP validation, and a derived section-ownership map.
category: Education
version: 1.0.0
author: Agents University (PROF.DATA.ENGINEERING, imhotep.persona)
---

Contract THESIS.DATA.ENGINEERING.COHORT.V1: "Cohort Thesis — Governed Enterprise Data Platform". Supervisor PROF.DATA.ENGINEERING; validator imhotep.persona. The original contract is `references/thesis_contract.v1.json`.

## Thesis question
Can this cohort design and defend an enterprise data platform whose data lineage, transformations, dependencies, reliability controls, governance, observability, AI-data interfaces, and recovery behavior are reconstructable from evidence?

## Eligibility (all required before thesis work is validated)
- Each of the 10 students has independently passed every required curriculum module or has an explicitly approved documented equivalent
- Every student has passed an unfamiliar transfer challenge
- Zero unresolved critical correctness, privacy, security, lineage, reproducibility, or governance defects
- All required module evidence is bound to student and cohort identities
- Professor has issued a disciplinary readiness recommendation

## Required sections and default owners
The ownership column is derived (`references/section-ownership.derived.json`); the professor assigns the final mapping.

| Section | Default owner(s) |
|---|---|
| `problem_and_decision_context` | DE-STU-010 |
| `source_and_data_contracts` | DE-STU-001 |
| `logical_and_physical_data_model` | DE-STU-002, DE-STU-007 |
| `batch_ingestion_and_transformation` | DE-STU-001 |
| `streaming_or_cdc_design` | DE-STU-003 |
| `orchestration_retry_idempotency` | DE-STU-005 |
| `data_quality_observability_and_lineage` | DE-STU-004, DE-STU-008 |
| `security_privacy_governance` | DE-STU-006 |
| `ai_data_infrastructure` | DE-STU-009 |
| `failure_injection_and_recovery` | DE-STU-004 |
| `operability_cost_and_capacity_assumptions` | DE-STU-010 |
| `tradeoffs_rejected_alternatives_and_unknowns` | DE-STU-010 |
| `reproducibility_package` | DE-STU-008 |
| `rollback_and_recovery_plan` | DE-STU-005 |
| `limitations_and_validity_boundaries` | DE-STU-010 |

## Contribution rule
All ten students must have a named, hashed contribution mapped to at least one thesis section, and the integrated thesis must explain cross-specialty dependencies.

Record each contribution as `{student, thesis_section, artifact path, sha256}`. The controller requires `sha256` and `thesis_section` for every contribution.

## Defense rule
The cohort must provide a defense artifact addressing evaluator challenges, contradictions, assumptions, evidence gaps, and at least one alternative architecture.

## How IMHOTEP validates
- **Dimensions:** identity_and_provenance_complete, required_evidence_present, a01_a12_continuity, dependency_integrity, critical_conflicts_resolved, independent_evaluation_present, student_contribution_coverage, reproducibility_package_present, rollback_available, limitations_explicit.
- **Outcomes:** VALIDATED, VALIDATED_WITH_CONDITIONS, HOLD, REJECTED.
- **Hard stops:** missing_required_evidence, unresolved_critical_failure, unattributed_student_contribution, self_evaluation_substituted_for_independent_evaluation, thesis_artifact_changed_after_validation_hash, missing_reproducibility_or_rollback_evidence.

## Student procedure
1. Draft your section(s) from your **evaluated** module artifacts only. Cite each artifact by path and hash.
2. Write an explicit **cross-specialty dependencies** subsection (what you rely on from which classmate, and what relies on you).
3. List limitations and unknowns.
4. Hash the final file and report `{student, section, path, sha256}`. Never change it after hashing without re-hashing and noting why.
5. Prepare for the defense: likely challenges, contradictions with other sections, and one alternative architecture for your area.
