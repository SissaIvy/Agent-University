---
name: IMHOTEP Task Codification
slug: imhotep-task-codification
description: Extract tasks from unstructured text into the Canonical Task Schema (A-coded container) and validate/fix existing task JSON with a fixlog.
category: Governance
version: 0.1.0
author: Agents University (imhotep.persona)
---

Turns unstructured material (emails, tickets, meeting notes, RFPs, PRs) into valid SISSA Task Objects, and repairs task JSON that fails the schema. The schema is in `references/task-object.schema.json`, a worked example is in `references/sample-tasks.json`, and the always-on overlay rules are in `references/overlay.json`.

## Procedure A: generate from text
1. **Name the role pack** (#SISSA, #Sera, #RealEstateInvestor, #GENIA, #SeniorAIScientist), or state that none applies and use the defaults.
2. **Read the source fully** (`fs.read` for files). Record where it came from; that string becomes every task's `source_reference`.
3. **Extract tasks.** One task per distinct commitment or deliverable. Do not invent tasks the source does not support. Note ambiguities in the summary instead.
4. **Assign A-codes** by lifecycle stage, as keys `A##_PascalName`. Never renumber existing keys.
5. **Fill the required fields:** `task_name`, `owner` (from the source; if absent use `"Unassigned"` and list it as an unknown), `status`, `source_reference`, and `memory_correlation {neuron, date, context}`.
   - `date` = today if the source gives none.
   - `context` ≤ 60 words **and** ≤ 320 chars.
   - `neuron` is a short stable concept id, e.g. `task_schema.v1`.
6. **Apply overlay defaults and rules** (`references/overlay.json`): priority P2, reasoning modes [Deterministic, Bayesian], status Pending; due within 3 days → P0; Review without artifacts → In Progress; Blocked requires dependencies + risk notes.
7. **Attach the role pack's KPIs** to `governance.kpi` and its preferred `reasoning_modes`.
8. **Return `{ "meta": {...}, "tasks": {...} }` only.** `meta` carries `version`, `generated_at` (ISO timestamp), `persona: "Imhotep"`, and `role_pack`.

## Procedure B: validate and fix
1. Check every task against the schema: required fields, enums, length limits, the dependency pattern `^A[0-9]{2}_.+`, and **no additional properties**.
2. Check the overlay rules (above).
3. If everything is valid, return the JSON unchanged with `meta.validation: "PASS"`.
4. If anything is invalid, return a corrected JSON with `meta.fixlog`: an array of `{task, field, issue, fix}`, one entry per change. Fix only what is needed; preserve provenance and keys. If a fix requires information you do not have (e.g. a missing owner), use a placeholder, set status to Blocked or Pending as the rules require, and record it in the fixlog as needing input.

## Rules
- Enums: status Pending | In Progress | Blocked | Review | Complete; priority P0–P3; risk Low | Medium | High; reasoning Bayesian | Deterministic | RHL | Socratic | Allegorical.
- Never fabricate artifacts, dates, owners, or metrics. Unknown stays unknown.
- Save the container with `fs.write` when the Commander wants to keep it, and log `schema_validation_pass_rate` observations in the notebook.

## Output
The JSON container (with `meta.fixlog` when fixing), then at most three lines of plain summary: tasks extracted or fixed, unknowns, and anything blocked.
