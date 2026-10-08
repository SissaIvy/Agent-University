---
name: University Promotion Governance
slug: university-promotion-governance
description: Decide Agents University library promotions on evidence - the librarian_promotion gate, the promotion policy, the A01-A12 stage checklist, the skills matrix and the incubator pack.
category: Governance
version: 0.1.0
author: Agents University (DeanLibrarian; authored for StarNet from docs/teachpacks and archetypes)
---

How the library decides promotions. The source policies are in `references/`: `promotion_policy.v1.json`, `stage_checklist.v1.csv`, `skills_matrix.v1.csv` and `incubator_pack.v0.1.0.json`. In this copy, stage A06's abbreviated name is spelled out as "Model/Evaluation"; everything else is verbatim from `docs/teachpacks/` and `archetypes/`.

## Gate: librarian_promotion (ApprenticeLibrarian → Librarian)
It requires all three, each shown by evidence-ledger entries:
- `teach_packs_emitted >= 50`: the sum of the `teach_packs_emitted` counts in `.mm-out/university/evidence.jsonl`.
- `report_built == true`: at least one `report_built` event.
- `audit_present == true`: an `audit_card` for the runs being counted.

## Promotion policy
- Minimum rubric level 3.
- Required evidence: audit_card, verify_outcome, gate_decision, rollback_ready.
- Coverage: courses tagged ≥ 0.9; skills covered ≥ 0.9.
- Stage requirements:
  - A04: source fetch (or its error) plus a written manifest.
  - A05: a data-quality issue or profiling report.
  - A08: gate decision, rollback ready, approver sign-off.
  - A10: execute started and completed, plus a verified outcome.

## Stage checklist (library variant of A01–A12)
| Stage | Must-have artifacts | Exit gate |
|---|---|---|
| A01 Discover | intake_record; owner; scope_seed | scope accepted with owner |
| A02 Frame | constraints; objectives; overlays | scope sign-off |
| A03 Plan | plan_doc; guardrails_plan; eval_plan | plan approved |
| A04 Data | source_list; provenance; evidence ledger | required sources present or skip with evidence |
| A05 Screen | profiling_report; schema_checks; normalization_log | quality acceptable or bounded |
| A06 Model/Evaluation | eval_runs; assumptions; metrics_report | meets threshold or defer |
| A07 Risk | risk_matrix; safety_check; pii_review | acceptable risk with mitigations |
| A08 Gate | gate_decision; rollback_ready; approvals | approved for canary |
| A09 Canary | canary_plan; monitoring; budget guards | canary success→promote or rollback |
| A10 Execute | runbook; execute logs; verify_outcome | applied with verification |
| A11 Monitor | observability dashboards; drift/freshness checks; kpi_snapshot | stable ops; anomalies ticketed |
| A12 Review | retrospective; lessons_learned; gate_update | closed loop; standards updated |

## Procedure
1. Read the evidence ledgers. Never accept a claimed count.
2. Optionally run `python scripts/teachpacks_validate.py` in the `aml` checkout. It writes `.mm-out/governance/promotion_report.json` and `.md`; exit 0 is pass, 1 is fail.
3. Decide **GO** or **HOLD**. List each requirement with its evidence path or "missing", and name the cheapest next step on a HOLD.
4. Write the decision to a file and note it in the notebook. Badges are updated by `scripts/update_badges.py`, not by hand.

## Incubator (only after GO)
The Incubator Pack ("Promote → Specialize → Replicate", owner DeanLibrarian):
- binds a PROMOTED agent to an occupational specialty;
- spawns at most 3 pupils with teach packs;
- requires rubric level ≥ 3 and the evidence audit_card, verify_outcome, gate_decision, rollback_ready;
- run with `python scripts/incubator_specialize_and_spawn.py`.

It needs the occupational-outlook CSV inputs under `.mm-out/bls/`. Report if they are absent.
