---
name: Codespace Devcontainer Setup
slug: codespace-devcontainer-setup
description: Set up, optimize and troubleshoot a reproducible GitHub Codespaces / devcontainer environment from a repository's requirements, with no secrets in files and a fresh-build check.
category: Engineering
version: 0.1.0
author: Agents University (CodespaceDeveloper; authored for StarNet from the profile README)
---

Procedure for the CodespaceDeveloper's capabilities: setup, devcontainer configuration, workspace management, optimization and troubleshooting.

## 1. Gather requirements
Read the repo's dependency files (`requirements*.txt`, `pyproject.toml`, `package.json`, lockfiles), CI config, and contributor docs. List runtimes with versions, system packages, services (databases, queues), editor extensions, forwarded ports, and **secret names** (never values).

## 2. Author `.devcontainer/devcontainer.json`
- Base: a maintained devcontainer image or a small Dockerfile. Prefer devcontainer *features* for common runtimes.
- Pin the runtime versions to match CI (e.g. Python 3.11 in CI vs 3.12 locally: pick one deliberately and say why).
- `postCreateCommand`: create the venv and install dependencies (e.g. `python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt`).
- `customizations.vscode.extensions`, e.g. `ms-python.python`, `ms-toolsai.jupyter`.
- `forwardPorts` for local services, bound to 127.0.0.1 where the app allows it.
- Secrets come from the platform's secret store; reference them by name only.

## 3. Verify with a fresh build
Build from the config alone (a new Codespace, or the devcontainer CLI) and run the project's tests or smoke checks. Record the build time, the test result, and anything that needed manual steps. Manual steps are defects to fix.

## 4. Optimize
- Order Dockerfile layers for caching.
- Enable prebuilds for slow setups.
- Use a slimmer base image.
- Right-size the machine type.
- Set idle timeouts.
- Measure before and after (build/start time, cost per hour).

## 5. Troubleshoot
Read the creation log first. Common causes: version mismatch with lockfiles, missing system libraries, post-create steps that need network or secrets, extension conflicts, port collisions. Fix the cause in config, not by hand in the running container, and document it.

## 6. Document
Write a short README next to the config: what it sets up, how to start, how to add a dependency, known issues and fixes.

## Rules
- No secrets in committed files.
- No destructive repo changes without approval.
- Never claim an environment works until a fresh build has passed.
