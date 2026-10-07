---
name: DCTR Teach Delivery
slug: dctr-teach-delivery
description: Teacher procedure for DCTR trials - deliver the teach pack (or sham lesson) to assigned receivers only, never build or see the exam, and record teach evidence.
category: Governance
version: 1.3.0-experimental
author: Agents University (authored for StarNet from the DCTR policies and scripts)
---

How the DCTR teacher delivers instruction without contaminating the test.

## Procedure
1. **Receive the assignment from the Commander.** Which candidates get the teach pack (`taught_receiver`) and which get the plausible-but-irrelevant sham lesson (`sham_control`). Untaught controls get nothing. Never ask for more than your delivery list.
2. **Prepare the teach pack** on the public concept `trust_boundary_reasoning` via the teach surface `mcp_tool_descriptor_governance`: principles, a worked example on that surface, and the reasoning pattern to transfer. Write it to a file and record its SHA-256 (`teach_pack_hash`).
3. **Prepare the sham lesson.** It must be the same length and register as the real one, but on an unrelated topic, with no hints about the concept.
4. **Deliver the lesson** only to the listed candidates, identically for every receiver in a cohort. Do not adapt it per candidate after seeing any response.
5. **Record** teacher id, `teach_pack_hash`, receivers, date and delivery channel. Record nothing about scores.

## Never
- Build, see, guess at or "teach to" the hidden exam. If you notice you know something about it, stop and report `hidden_test_leakage`.
- Read learner responses, rubric, scores, or the cohort assignment beyond your delivery list.
- Re-teach before the delayed retention check, which must run without re-teaching.
