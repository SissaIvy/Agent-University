---
name: DCTR Hidden Scenario
slug: dctr-hidden-scenario
description: Scenario generator procedure for DCTR - build sealed pre-test, hidden cross-domain transfer, adversarial mutation and retention items plus rubric, avoid forbidden terms, and hash everything before any learner sees a prompt.
category: Governance
version: 1.3.0-experimental
author: Agents University (authored for StarNet from the DCTR policies and scripts)
---

How the isolated scenario generator builds the exam. The full policy is in `references/security_mastery_dctr.v1.1.json`. **This skill is sealed material: never share it, or anything derived from it, with the teacher, learners or evaluator before sealing.**

## The concept and its surfaces
- Concept: `trust_boundary_reasoning`.
- Taught on: `mcp_tool_descriptor_governance`.
- Hidden test on: `multi_agent_saas_connector_incident`, a materially different domain.
- Forbidden exam terms (these must not appear in any learner-facing prompt): `mcp`, `poison`, `trust boundary`, `trust-boundary`, `tool metadata`.

## Build
1. **Pre-test item:** probes the concept in neutral form before teaching, so a baseline can be measured.
2. **Hidden transfer item:** a realistic incident on the hidden surface where the taught principle is the key to a good answer, but it is never named. Scan the text for the forbidden terms and their obvious synonyms.
3. **Adversarial mutation:** a variant with misleading evidence or distractors, to test robustness.
4. **Retention item:** an isomorphic but new item for the delayed check, used without re-teaching.
5. **Rubric:** signals per item (what a strong answer contains), the scoring scale (0–1), critical-error definitions, and `rubric_version`.
6. **Seal:** write the items and rubric to a sealed file, compute SHA-256 hashes (`pretest_hash`, `hidden_scenario_hash`, the rubric configuration hash; compact JSON with sorted keys), and hand the sealed file to the Commander only.
7. **Public catalog:** a separate file containing only the trial id, the concept id, the teach surface, and a note that learners receive public prompts at runtime.

## Never
- Talk to the teacher, learners or evaluator about the exam.
- See learner responses before sealing, or know the cohort assignment.
- Reuse a previously administered item. A replayed experiment is a reject code (`replayed_successful_experiment`).
