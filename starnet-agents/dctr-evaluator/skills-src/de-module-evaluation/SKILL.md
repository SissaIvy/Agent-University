---
name: DE Module Evaluation
slug: de-module-evaluation
description: Independent evaluator procedure for Data Engineering cohort module and transfer submissions - score six dimensions, apply the critical failure rule, and write the evaluation JSON the cohort controller accepts.
category: Governance
version: 1.3.0-experimental
author: Agents University (authored for StarNet from the DCTR policies and scripts)
---

How to independently evaluate a Data Engineering student's module or transfer submission (cohort DE-2026-09-29). The module objectives and required artifacts are in the `de-curriculum` skill.

## Independence check (first)
Your evaluator id must not be the student, PROF.DATA.ENGINEERING, or imhotep.persona; the controller rejects those. You must not have taught, mentored, or peer-reviewed this submission. Declare any conflict and stop.

## Procedure
1. **Load the module** from `de-curriculum`: objective and required artifacts.
2. **Check completeness:** every required artifact present, and hashes in the student's `submission_manifest.json` match the files you received.
3. **Score the six dimensions** with evidence (cite file and section): correctness, traceability, dependency_integrity, governance, failure_handling, explainability. For each, give pass/fail and a basis.
4. **Separate executed from proposed.** Claims marked executed must have output evidence; otherwise treat them as proposed and note it.
5. **Check failure injection** for pipeline and orchestration modules (DE300, DE500 and similar), when execution was available.
6. **Apply the critical failure rule:** any unresolved critical correctness, security, privacy, lineage, or reproducibility defect means `passed: false`, whatever the other scores.
7. **Transfer challenges:** confirm the scenario was unfamiliar and no worked solution was available. Judge whether the principle was genuinely applied, not pattern-matched.

## Evaluation JSON (the controller requires `evaluator_id`, boolean `passed`, list `critical_failures`)
    { "evaluator_id": "<your evaluator id>", "student_id": "DE-STU-0NN", "module": "DE###",
      "passed": false, "critical_failures": [{"type": "lineage", "detail": "…", "location": "…"}],
      "dimensions": {"correctness": {"pass": true, "basis": "…"}, "traceability": {"pass": false, "basis": "…"}},
      "executed_vs_proposed_notes": "…", "remediation": ["…"], "evaluated_at": "…" }

Save it as a file. The Commander records it with `evaluate --student … --module … --result <file>`, or with `evaluate-transfer` for transfer challenges.

## Never
- Alter a student submission.
- Give formative teaching; that is the professor's job. Remediation notes stay short and factual.
- Issue thesis validation; that belongs to IMHOTEP.
