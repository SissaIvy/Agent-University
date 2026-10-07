---
name: University Library Workflow
slug: university-library-workflow
description: Run the Agents University library workflow - consented local scans of notebooks and code, track classification, catalog and report builds, and teach-pack emission - with audit cards and append-only evidence.
category: Knowledge
version: 0.1.0
author: Agents University (library staff; authored for StarNet from scripts/university_workflow.py)
---

The library's discovery, catalog and teach procedure, as implemented by `scripts/university_workflow.py` in the `aml` repo (wrapper: `scripts/university.ps1`). It runs in the Commander's checkout via the terminal, only with consent.

## Modes
- `scan`: discover `.ipynb`/`.py` files under the roots and classify each by its imports. Writes `notebooks_index.jsonl` (skipped with `--dry-run`).
- `build`: scan, then build `catalog.json` (one course per track; lessons = notebooks) and a summary report.
- `teach`: build, then emit `<lesson>.teach.json` per notebook into `.mm-out/university/teach-packs/`.
- `all`: scan and build.

Options: `--roots "<p1>;<p2>"`, `--max-files N` (default 2000), `--include "<globs>"`, `--exclude "<globs>"`, `--dry-run`, `--yes` (skip the prompt; use only after the Commander approved the plan).

## Tracks (import-based classification)
foundations, ml-core, deep-learning, nlp, cv, rl, llms-rag, mlops. For example, torch/tensorflow → deep-learning; transformers/langchain/faiss → llms-rag; spacy/nltk → nlp; opencv/ultralytics → cv; gym/stable_baselines3 → rl; sklearn/xgboost → ml-core; mlflow/airflow/fastapi → mlops; anything else → foundations.

## Procedure
1. **Plan and consent.** State the roots, include/exclude globs and max files. Always exclude `.venv`, `node_modules`, `.ipynb_checkpoints`, `.git` and system folders. Get the Commander's yes.
2. **Dry run first** on any new scope: `python scripts/university_workflow.py scan --roots "<roots>" --dry-run --yes`. Report the candidate counts.
3. **Run the real mode** (`scan`, `build` or `teach`) with the same roots.
4. **Check the evidence** in `.mm-out/university/evidence.jsonl`: an `audit_card`, then `scan_started`, `scan_summary`, and (by mode) `catalog_built`, `report_built`, `teach_packs_emitted` with a count.
5. **Review the output.** Spot-check classifications and a sample of teach packs. The generated objectives and exercises are generic templates and usually need curation.
6. **Report** counts by track, notable lessons, misclassifications fixed, and the evidence file paths.

## Teach-pack shape
`{"title", "path", "track", "tags", "imports", "objectives": [3], "exercises": [3]}`

## Guardrails
- Local-only: nothing leaves the machine.
- Fail-closed: no audit card means the run is not trusted.
- Never rewrite evidence lines.
- The audit-card atlas spec (`archetypes/atlas_agent_platform.v0.1.0.json`) is absent from the repo, so cards fall back to agent id `AGT.MM.UNI`. Note it in reports.
