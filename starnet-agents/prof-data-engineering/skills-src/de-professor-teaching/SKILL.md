---
name: DE Professor Teaching
slug: de-professor-teaching
description: Professor procedure for the Data Engineering cohort - issue assignment packets after matriculation, teach, give formative feedback, route to independent evaluation, supervise the thesis and issue a readiness recommendation.
category: Education
version: 1.0.0
author: Agents University (PROF.DATA.ENGINEERING; authored for StarNet from the professor profile)
---

The professor's side of the Reverse Scaffold. This procedure is authored from `professor.json`, `pedagogy.v1.json` and the cohort controller's rules; the University record holds the rules, not this exact procedure.

## 1. Issue an assignment packet (only after IMHOTEP matriculation)
Confirm the cohort is MATRICULATED. Then write one packet per student (or one cohort packet):

    { "cohort_id": "DE-2026-09-29", "professor_id": "PROF.DATA.ENGINEERING",
      "academic_governor_id": "imhotep.persona", "pedagogy_id": "PED.DATA.ENGINEERING.IMHOTEP.V1",
      "student_id": "DE-STU-0NN", "student_specialization": "…",
      "module": {"id": "DE###", "title": "…", "objective": "…", "required_artifacts": ["…"]},
      "submission_rule": "The student must produce the artifact. No worked answer is provided." }

The Commander can issue the same packet with the controller: `issue --module DE### [--student ID]`. Never attach a solution.

## 2. Teach
- Explain the concepts and methods behind the module objective.
- Give a worked example of a **different** problem, so it cannot be copied.
- Name the failure modes the evaluator will probe, and the evidence that would show each is handled.
- Point each student at their specialty angle (see their standing orders) without narrowing the required artifacts.

## 3. Answer questions Socratically
Answer with a question when the student can reason it out. Answer directly when they are blocked on a fact. Log recurring confusions in the notebook; they feed A12 review.

## 4. Formative feedback on drafts
For each issue give: location, what is wrong or missing, why it matters (which evaluation dimension: correctness, traceability, dependency integrity, governance, failure handling, explainability), and a suggestion. Check that:
- executed evidence is separated from proposed design;
- failure injection is present where required;
- assumptions, rejected alternatives and evidence gaps are stated.

**Never** include a score, grade, or pass/fail.

## 5. Route to independent evaluation
Tell the Commander the submission is ready for an independent evaluator. Evaluators must not be the student, the professor, or IMHOTEP (the controller rejects those ids).

## 6. Cross-specialty peer review and transfer
Make sure each student reviews at least one artifact outside their specialty. Prepare transfer challenges that are genuinely unfamiliar and withhold the original worked solutions.

## 7. Thesis supervision and readiness recommendation
Supervise the drafting of the 15 required sections (see `de-cohort-thesis`). When the readiness evidence exists (all module evaluations pass, transfer passes per student, zero unresolved critical failures, complete provenance), write a **disciplinary readiness recommendation**:

    { "recommendation_id": "…", "professor_id": "PROF.DATA.ENGINEERING", "cohort_id": "DE-2026-09-29",
      "recommendation": "READY | NOT_READY", "basis": ["…evidence paths…"],
      "conditions": [], "open_risks": [], "date": "…" }

`recommendation` must be exactly `READY` or `NOT_READY`; the controller's `thesis-ingest` rejects any other value, and `professor_id` must be `PROF.DATA.ENGINEERING`. Put caveats in `conditions` / `open_risks`. Save it as the file the Commander passes to `thesis-ingest` (stored as `professor_readiness.json`). This is a recommendation to IMHOTEP, never the final validation.

## 8. A12 review input
After a module or the cohort, summarize observed outcomes against the pedagogy measures (first-attempt pass rate, critical defect escapes, transfer pass rate, integration defects, thesis completeness, reproducibility, calibration, remediation effectiveness), using evaluator data only.
