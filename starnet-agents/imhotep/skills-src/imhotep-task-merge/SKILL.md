---
name: IMHOTEP Task Merge
slug: imhotep-task-merge
description: Merge proposed tasks into an existing A-coded task container without renumbering, preserving provenance and resolving key collisions with suffixes and dependencies.
category: Governance
version: 0.1.0
author: Agents University (imhotep.persona)
---

Folds newly extracted or proposed tasks into an existing container so history and provenance survive.

## Procedure
1. **Validate both inputs** against the Canonical Task Schema first (use the codification skill). Merging invalid records spreads defects.
2. **Match by A-code key.**
   - **New key:** add the task as-is.
   - **Same key, same task** (same intent and source): update only the fields the proposal changes. Keep the original `source_reference` and `memory_correlation`. Bump `audit.last_updated_at`. Record the change.
   - **Same key, different task (collision):** do **not** overwrite. Create a suffixed key (e.g. `A06_ValidationCI` → `A06_ValidationCI_b`, then `_c`…). Add the original key to the new task's `governance.dependencies`.
3. **Never renumber** existing keys and never delete a task. Retire one by setting status Complete, or Blocked with a reason, as the evidence supports.
4. **Re-apply the overlay rules** after merging (due within 3 days → P0, Review without artifacts → In Progress, Blocked needs dependencies + risk notes).
5. **Produce a merge proposal**, not a silent overwrite:

       { "meta": {"merged_at":"…","base_source":"…","proposal_source":"…"},
         "added": ["A08_…"], "updated": [{"key":"A06_…","fields":["status"]}],
         "collisions": [{"original":"A06_…","new_key":"A06_…_b"}],
         "result": { "meta": {...}, "tasks": {...} } }

## Rules
- Provenance is sacred: a merged task keeps every source reference it ever had. If two sources matter, link the second as an artifact.
- Ask before applying a merge to a file someone else owns; offer the proposal instead.
- Save the proposal with `fs.write`. Only apply it to the live container when the Commander approves.

## Output
The merge proposal JSON, then a short summary of counts (added / updated / collisions) and anything needing a decision.
