---
name: DE Module Work
slug: de-module-work
description: Student procedure for completing a Data Engineering module under the Reverse Scaffold pedagogy - artifacts, failure injection, submission manifest, peer review and transfer challenge, with no self-grading.
category: Education
version: 1.0.0
author: Agents University (PROF.DATA.ENGINEERING with imhotep.persona)
---

How a Data Engineering student turns an assignment into an evaluable submission, under pedagogy PED.DATA.ENGINEERING.IMHOTEP.V1 (`references/pedagogy.v1.json`).

## Educational thesis
Students should not be promoted for reproducing explanations. They must produce traceable data-engineering artifacts, survive failure-oriented evaluation, transfer principles to unfamiliar conditions, and integrate the cohort's specialties into a defensible final thesis.

## Instructional methods (rules)
- **evidence_first_lab**: Every technical claim tied to a working artifact must distinguish executed evidence from proposed design.
- **failure_injection**: Core pipeline/orchestration modules require at least one controlled failure case and recovery analysis when execution is available.
- **socratic_design_defense**: Students must state assumptions, rejected alternatives, dependencies, risks, and evidence gaps.
- **cross_specialty_peer_review**: Each student must review at least one artifact outside its specialization; peer review is advisory and cannot replace independent evaluation.
- **transfer_challenge**: Before thesis eligibility, each student must apply a learned principle to an unfamiliar data-engineering scenario without access to the original worked solution.
- **cohort_integration**: The final thesis must integrate contributions from all ten student specialties into one coherent governed platform argument.

## Procedure for one module
1. **Discover.** Read the assignment packet (module, objective, required artifacts, your specialization). List sources, owners, constraints and unknowns.
2. **Model.** Write the design: entities, flows, contracts, dependencies. State assumptions and **rejected alternatives**.
3. **Build.** Produce each required artifact as a real file (`fs.write`). Code, SQL, configs, designs, and test definitions all count.
4. **Break.** Inject at least one controlled failure (pipeline and orchestration modules always; others when meaningful), e.g. bad record, late data, duplicate delivery, schema change, permission denial, partial run.
5. **Diagnose.** Show how the failure was detected and what the evidence was.
6. **Repair.** Fix it, and show the recovery evidence or recovery plan.
7. **Explain.** Write a plain explanation a reviewer can follow. Every claim is labelled *executed* (with output) or *proposed* (not run).
8. **Transfer.** Name the principle the module taught and where else it applies.
9. **Defend.** Answer the likely evaluator challenges: assumptions, contradictions, evidence gaps, risks.

## Submission manifest (write it as `submission_manifest.json` next to the artifacts)
    { "student_id": "DE-STU-0NN", "module": "DE###", "specialization": "…",
      "artifacts": [{"name": "<required_artifact>", "path": "…", "sha256": "<if computed, else null>",
                     "status": "executed|proposed", "evidence": "…"}],
      "failure_injection": {"case": "…", "detected_by": "…", "recovery": "…", "executed": true},
      "assumptions": [], "rejected_alternatives": [], "dependencies": [], "risks": [],
      "evidence_gaps": [], "not_executed": [], "peer_review_requested_from": "DE-STU-0NN" }

Never include a score, grade, or pass field. Those belong only to the independent evaluator.

## Peer review (outside your specialization)
Review the artifact, not the person. Write findings with location, why it matters from your specialty, a suggested fix, and what you could not verify. Peer review is advisory and cannot replace independent evaluation.

## Transfer challenge (before thesis eligibility)
Given an unfamiliar scenario, without the original worked solution:
1. State the principle you are transferring.
2. Apply it.
3. Show the evidence.
4. List what did not transfer cleanly.

If the scenario is familiar, say so; it would not count.

## Handover
Tell the Commander the submission is ready and give the manifest path. They record it with the cohort controller (`ingest`). Evaluation is recorded separately by an independent evaluator.
