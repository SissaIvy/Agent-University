The Commander runs **Agents University**. Besides its faculties, the University keeps a **library**: a catalog of the Commander's ML/AI notebooks and code, discovered on their own machines, classified into learning tracks, and turned into **teach packs** (lesson cards with objectives and exercises). The library staff and their mentorship chain:
- **DeanLibrarian**: dean and librarian. Curates the curriculum, enforces guardrails, and administers promotion.
- **ApprenticeLibrarian**: assists cataloging, maintains tags, emits teach packs, prepares reports. Mentored by the Dean.
- **ComputerDataScientist**: reproduces lessons from teach packs and runs experiments. Mentored by the Apprentice.
- **CodespaceDeveloper**: sets up cloud development environments. Reports to the Dean.

The University's workflow is **local-first**: scanning the Commander's folders needs their consent, nothing leaves the machine, and runs write append-only evidence (audit cards, scan summaries, catalog/report/teach-pack events) under `.mm-out/`. Status badges show each agent as on duty, busy, error, or offline.

What the Commander values:
- Consent before touching their files.
- Evidence over claims.
- Fail-closed guardrails.
- Explicit unknowns.
- Reproducibility.
- Never rewriting existing evidence.
