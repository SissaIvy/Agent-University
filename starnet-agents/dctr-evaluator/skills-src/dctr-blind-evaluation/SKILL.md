---
name: DCTR Blind Evaluation
slug: dctr-blind-evaluation
description: Evaluator procedure for DCTR - score anonymized Candidate-* responses against the sealed rubric without seeing cohort or treatment, never constructing the exam, and record scores with hashes.
category: Governance
version: 1.3.0-experimental
author: Agents University (authored for StarNet from the DCTR policies and scripts)
---

Blind scoring for DCTR trials. The evaluator id is in your standing orders.

## Inputs (and only these)
`candidate_id`, `response_hash` and `response_text` for each candidate, plus the sealed rubric (version, signals) handed over by the Commander at scoring time.

## Procedure
1. **Verify integrity:** recompute the SHA-256 of each response and compare it with `response_hash`. A mismatch means do not score that item; report `evidence_tampering`.
2. **Check blinding:** if any input reveals cohort, treatment, teach pack or agent specialty, stop and report `evaluator_contamination`. Do not score.
3. **Score each response** independently against the rubric on a 0–1 scale, with a one-line basis per rubric signal. Score in random order, never side by side by cohort.
4. **Flag critical errors** separately (e.g. unsafe recommendations, fabricated evidence). They are counted, not averaged away.
5. **Record:** evaluator id, `rubric_version`, and per candidate `{candidate_id, response_hash, score, critical_errors, basis}`. Hash the score file.
6. **Hand the scores to the Commander for the gatekeeper.** You never see the unblinding.

## Never
- Construct, modify or suggest exam items.
- Receive treatment labels, or try to infer them.
- Re-score after unblinding.

## Thresholds the gate will apply (for context; you do not decide)
Hidden scenario score at least 0.9; retention at least 0.85; critical errors at most 0.
