# Agent Eval — Agent Evaluation & Observability

Agent evaluation harness and observability dashboard. Measures agent performance
(latency, token usage, success rate, error classification per agent) and traces
every tool call (allowed / denied / approval). Includes a continuous evaluation
suite for RAG and workflow outputs.

## Features

- Agent Metrics — latency, token usage, success rate, error classification
- Tool Observability — trace every call with input/output and decision
- Continuous Eval — benchmark scenarios tracking RAG quality over time
- Audit Integration — audit log format shared with AgentGuard

## Quickstart

```bash
git clone https://github.com/we-do-care-global/agent-eval.git
cd agent-eval
pip install -e .
pytest
```

## Architecture

- Python package (installable with `pip install -e .`)
- Web dashboard deployed via `docs/` on GitHub Pages
- Integration point: audit format aligned with AgentGuard

## Deploy / CI

- GitHub Pages: `docs/` (legacy branch source)
- CI workflow: `.github/workflows/ci.yml`
- Zenodo deposit: `.github/workflows/zenodo.yml`
- Pages URL: https://we-do-care-global.github.io/agent-eval/

## Metadata

- License: Apache 2.0
- ORCID: 0009-0009-8515-2727
- Citation: see `citation.cff`
- Zenodo archive: `.zenodo.json`
- Version: v0.1.0 (see `.zenodo.json` for latest release mapping)
