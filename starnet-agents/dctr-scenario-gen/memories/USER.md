The Commander runs **Agents University** and acts as the **Operator** of DCTR trials (the policy's owner role). The Commander assigns roles, routes material between roles so that blinding holds, runs the scripted steps in the `aml` checkout, and keeps the append-only evidence.

The DCTR crew on this station:
- **DCTR-Teacher** (`AGT.MCP.Security`)
- **DCTR-Learner** instances (`LRN.cohort.executor`), one per anonymized candidate
- **DCTR-ScenarioGen** (`SCN.GEN.independent`)
- **DCTR-Evaluator** (`EVAL.independent.blind`)
- **DCTR-Gatekeeper** (`GATE.university`)

Other University authorities:
- **IMHOTEP**: academic governor and A-code gate custodian.
- **PROF.DATA.ENGINEERING** and the DE students: the Data Engineering cohort, whose module and transfer submissions also need an independent evaluator.

What the Commander values:
- Evidence over claims.
- Separation of authority.
- Blinding that holds.
- Failed attempts preserved, never overwritten.
- An honest HOLD rather than a premature CERTIFIED.
