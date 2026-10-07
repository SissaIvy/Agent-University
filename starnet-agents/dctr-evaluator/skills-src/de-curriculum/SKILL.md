---
name: DE Curriculum v1
slug: de-curriculum
description: The Agents University Data Engineering curriculum CURR.DATA.ENGINEERING.V1 - ten modules DE100 to DE1000 with objectives, required artifacts, evaluation dimensions and the critical failure rule.
category: Education
version: 1.0.0
author: Agents University (PROF.DATA.ENGINEERING)
---

The full Data Engineering & Intelligent Data Infrastructure curriculum (v1.0.0). Professor PROF.DATA.ENGINEERING; academic governor imhotep.persona. The original record is `references/curriculum.v1.json`.

## Modules (in sequence)
1. **DE100 Data Contracts & Source Discovery**: Define sources, owners, schemas, SLAs, and evidence boundaries. Required artifacts: `source_inventory`, `data_contract`.
2. **DE200 SQL & Relational Modeling**: Design normalized and analytical relational models and demonstrate query correctness. Required artifacts: `schema_design`, `sql_artifact`, `validation_results`.
3. **DE300 Batch ETL/ELT Pipelines**: Build an idempotent batch pipeline with explicit inputs, outputs, failure behavior, and tests. Required artifacts: `pipeline_artifact`, `test_results`, `run_evidence`.
4. **DE400 Warehouse & Lakehouse Modeling**: Design governed analytical storage with dimensional or equivalent modeling and lineage. Required artifacts: `architecture_record`, `model_artifact`, `lineage_map`.
5. **DE500 Orchestration, Retry & Idempotency**: Demonstrate dependency control, retry safety, deduplication, and recovery. Required artifacts: `orchestration_artifact`, `failure_injection_evidence`, `recovery_evidence`.
6. **DE600 Streaming & Change Data Capture**: Design an event/CDC pipeline with ordering, replay, schema evolution, and failure controls. Required artifacts: `stream_design`, `schema_evolution_plan`, `replay_evidence`.
7. **DE700 Data Quality, Observability & Lineage**: Implement measurable quality rules, observability, incident evidence, and lineage. Required artifacts: `quality_contract`, `observability_artifact`, `lineage_evidence`.
8. **DE800 Governance, Privacy & Security**: Apply least privilege, classification, retention, access controls, and auditability. Required artifacts: `governance_matrix`, `access_model`, `audit_evidence`.
9. **DE900 AI Data Infrastructure**: Design ingestion, provenance, retrieval, embedding/vector, evaluation-data, or agent-memory infrastructure without losing source traceability. Required artifacts: `ai_data_architecture`, `provenance_record`, `evaluation_plan`.
10. **DE1000 Enterprise Data Platform Capstone**: Integrate the curriculum into an unfamiliar enterprise data-platform problem and defend the design under independent review. Required artifacts: `capstone_architecture`, `working_artifact_or_executable_plan`, `test_evidence`, `rollback_plan`.

## Every module
- **Learning cycle:** Discover → Model → Build → Break → Diagnose → Repair → Explain → Transfer → Defend.
- **Evaluator:** an independent evaluator, never the student, the professor, or IMHOTEP.
- **Evaluation dimensions:** correctness, traceability, dependency integrity, governance, failure handling, explainability.
- **Critical failure rule:** any unresolved critical correctness, security, privacy, lineage, or reproducibility defect blocks module passage.

## Transfer requirement
Each student must independently apply a learned principle to an unfamiliar data-engineering scenario before cohort-thesis eligibility.

## Completion rule
Program completion requires real student-produced artifacts for every module, independent evaluation, per-student transfer evidence, a cohort thesis, the professor's disciplinary readiness recommendation, and IMHOTEP final thesis validation. Matriculation or assignment issuance is not evidence of learning.

## How to use this skill
When working module X:
1. Look up its objective and required artifacts here.
2. Produce every artifact (the `de-module-work` skill has the procedure).
3. Apply your specialty lens from your standing orders.
