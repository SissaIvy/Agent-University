University record for CodespaceDeveloper, carried from the `aml` repo (snapshot 2026-10-07). This is context, not station truth.

### Profile
- Source: `agents/profiles/codespace_developer/agent.yaml` and `README.md`.
- Reports to DeanLibrarian. No apprentices (an entry-level specialization).

### Known gaps
- The declared tools `codespace_config_manager`, `devcontainer_builder`, `environment_optimizer` and `workspace_analyzer` have **no implementation** in the repo. The README's `scripts/codespace_config_manager.ps1` example does not exist.
- The `aml` repo has **no `.devcontainer/`** yet.
- No University badge file exists for me (the badge script covers only the three library agents).

### The README's example intent
Set up a Codespace for the AML repository with the profile `codespace_developer`, environment python3.11, and extensions `ms-python.python` and `ms-toolsai.jupyter`.

### Environment facts about `aml` worth knowing
- Python 3.12 locally, 3.11 in CI.
- Dependencies in `requirements.txt` and `requirements-dev.txt`. A fresh Ubuntu image needs `python3.12-venv` before `python3 -m venv` works.
- Tests spawn the literal command `python`, so the venv must be active (or `python` must be on PATH).
- The Streamlit dashboard should bind to 127.0.0.1.
