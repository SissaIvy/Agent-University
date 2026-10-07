---
name: Teach Pack Reproduction
slug: teach-pack-reproduction
description: Reproduce a lesson from an Agents University teach pack deterministically, compare one variant at a time, and write an evidence-backed experiment log.
category: Data Science
version: 0.1.0
author: Agents University (ComputerDataScientist; authored for StarNet from the profile and teach-pack format)
---

Turns a teach pack (`.mm-out/university/teach-packs/<lesson>.teach.json`: title, path, track, tags, imports, objectives, exercises) into a verified result.

## Procedure
1. **Read the pack and the notebook** (`path`). Write down the one core result you will reproduce and how you will know it matches.
2. **Pin the environment.** Record Python and key library versions (from `imports`), hardware notes and seeds. Create an isolated environment when possible.
3. **Run twice** with the same seed. Record both outputs and whether they match (and the tolerance used, for floating-point results).
4. **Do the exercises:**
   - Add a test cell that validates a core function.
   - Swap **one** model or library variant, keep data and seed fixed, and compare on metrics declared before the run.
   - Document failure modes and the retries you made.
5. **Build a dataset only if needed.** Record source, license, size, splits and checksums. Use no personal data without explicit approval.
6. **Write the experiment log** as a file next to the outputs.

## Experiment log shape
    { "lesson": "…", "teach_pack": "<path>", "goal": "…", "environment": {"python": "…", "libs": {}, "seed": 0},
      "runs": [{"id": "r1", "result": "…"}, {"id": "r2", "result": "…"}], "deterministic": true,
      "variants": [{"change": "…", "metric": "…", "baseline": "…", "variant": "…"}],
      "failures": [{"error": "…", "suspected_cause": "…", "next_step": "…"}],
      "finding": "…", "not_executed": [] }

## Rules
- Never report a number you did not compute, and say on what data it was computed.
- A failed reproduction is a valid finding. Report it to your mentor as a possible teach-pack defect.
- Never rewrite earlier logs; add a new run.
