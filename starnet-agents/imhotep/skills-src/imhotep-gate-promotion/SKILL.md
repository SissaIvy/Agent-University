---
name: IMHOTEP Gate Promotion
slug: imhotep-gate-promotion
description: Promote A-coded tasks through the A06 evaluate, A07 risk, A08 options and A09 decision gates with evidence, rubric, outcome, follow-ups and rollback.
category: Governance
version: 0.1.0
author: Agents University (imhotep.persona)
---

Moves tasks through IMHOTEP's gates and produces a gate report for each one. A gate passes on evidence, never on assertion.

## Inputs
A tasks container (Canonical Task Schema), the gates requested (any of A06, A07, A08, A09), and the evidence available: artifacts, metrics, and evaluation results.

## Procedure
1. **A06 Evaluate** (Bayesian, Deterministic, RHL).
   - Attach the relevant KPIs and link the evaluation artifacts.
   - If the evaluation evidence passes, set status to Review. If artifacts are missing, status stays (or drops to) In Progress.
   - The evaluator must not be the task's author.
2. **A07 Risk** (Bayesian, Deterministic).
   - Reassess `governance.risk.level` (Low | Medium | High) and write mitigation notes (≤ 200 chars).
   - Name the risk tags from the role pack that apply.
3. **A08 Options** (Bayesian, RHL, Socratic).
   - Record at least two genuinely different options, each with assumptions and tradeoffs, ranked.
   - Ask, Socratically, what would make the top option wrong.
4. **A09 Decision gate** (Deterministic + Socratic; Allegorical optional for alignment).
   - Require the **evidence set**: artifacts **and** metrics.
   - Require a **rollback plan**.
   - Check the hard stops: unauthorized action, missing required evidence, unresolved critical conflict, irreversible action without approval, audit failure, cross-mission contamination.
   - Outcome is one of GO, GO_WITH_CONDITIONS, HOLD, NO_GO, ESCALATE. Any hard stop → never GO.
   - IMHOTEP does not choose a business option when the evidence is missing. That is HOLD, with the missing evidence named.

## Gate report shape
For each gated task, add a gate block to the task's companion report (not inside the schema-strict task object, which forbids extra properties):

    { "task": "A09_…", "gate": "A09_decision_gate", "reasoning_modes": ["Deterministic","Socratic"],
      "evidence": [{"type":"…","label":"…","url":"…"}], "metrics": {"…": "…"},
      "options": [{"id":"O1","summary":"…","tradeoffs":"…"}], "rubric": ["…"],
      "hard_stops_checked": {"missing_required_evidence": false, "…": false},
      "outcome": "HOLD", "conditions": [], "follow_ups": ["…"], "rollback": "…",
      "basis": "…", "unknowns": ["…"], "decided_at": "…" }

Save the report as markdown or JSON with `fs.write`, under a gates folder in the project the Commander names. Write follow-ups back as new A-coded tasks via the codification skill.

## Rules
- The autonomy ceiling is L2 (bounded, reversible) unless the Commander grants more. An irreversible action always needs explicit approval.
- Preserve conflicts in the report; never average them away.
- Track `gate_defect_escape_rate` and `decision_evidence_completeness_score` in the notebook from observed outcomes only.
- These gate verdicts are advisory on this station; say so when a verdict could be read as enforcement.

## Output
The gate report(s), then one line per task: gate, outcome, and the single most important missing item (if any).
