# se-paper-writing

Software engineering paper writing skill for ICSE, ESEC/FSE, ASE, ISSTA, MSR, TSE, TOSEM, and EMSE.

## What this skill does

This skill helps turn a research repo and experiment outputs into a submission-ready SE paper by guiding:

- Venue-aware paper planning for conferences vs journals.
- Claim-to-evidence structuring (research questions, metrics, baselines, and threats to validity).
- Citation safety with DOI-first BibTeX retrieval and explicit placeholders when unresolved.
- Submission and camera-ready quality checks with practical checklists.

In short: it is a workflow + tool bundle for writing rigorous SE papers without relying on stale venue rules or fabricated citations.

## Typical prompts this skill is built for

- "Draft an ICSE paper from this repository."
- "Convert this FSE paper into a TSE journal submission plan."
- "Help me structure threats to validity and statistical reporting."
- "Fetch verified BibTeX for these references."
- "Run a final pre-submission checklist for ASE."

## Claude agent skills docs

For protocol-level details on how agents should trigger and apply this skill, see:

- [`docs/claude-agent-skills.md`](docs/claude-agent-skills.md)

## What this repo contains

- `SKILL.md`: Core skill instructions and workflow.
- `docs/claude-agent-skills.md`: Agent-oriented protocol and maintenance contract.
- `references/`: Venue routing, evaluation playbook, checklists, reviewer guidance, citation workflow, and official source links.
- `scripts/fetch_templates.py`: Fetch template resources by venue from `references/template-sources.json`.
- `scripts/doi_to_bibtex.py`: Fetch verified BibTeX from a DOI.
- `assets/se_skeleton/`: Lightweight LaTeX skeleton and table stubs.

## Key principles

- Verify venue requirements from official sources in-session before applying rules.
- Never hallucinate citations; use DOI-first retrieval and placeholders when unresolved.
- Build claim-evidence mapping before prose.

## Quick usage

```bash
# Validate skill structure
python3 /Users/romel/.codex/skills/skill-creator/scripts/quick_validate.py /Users/romel/.codex/skills/se-paper-writing

# Dry-run template retrieval
python3 scripts/fetch_templates.py --dry-run --all --dest /tmp/se-templates

# Fetch BibTeX by DOI
python3 scripts/doi_to_bibtex.py --doi 10.48550/arXiv.1706.03762
```
