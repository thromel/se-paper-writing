# se-paper-writing

Software engineering paper writing skill for ICSE, ESEC/FSE, ASE, ISSTA, MSR, TSE, TOSEM, and EMSE.

## What this repo contains

- `SKILL.md`: Core skill instructions and workflow.
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
