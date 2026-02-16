# Claude Agent Skills Protocol

This document explains how this repository is intended to be used as a Claude/Codex skill.

## Trigger Contract

Skill triggering depends on `SKILL.md` frontmatter:

- `name`: `se-paper-writing`
- `description`: when-to-use conditions for SE paper workflows

The `description` should stay trigger-focused. Do not replace it with process details.

## Skill Structure Contract

- `SKILL.md`: core operating workflow and non-negotiable rules
- `references/`: heavy reference material loaded only when needed
- `scripts/`: deterministic helpers for repeatable tasks
- `assets/`: starter artifacts used in outputs

Use progressive disclosure: keep `SKILL.md` concise and link out to references for detail.

## Runtime Protocol for Agents

1. Confirm the user request matches SE paper-writing scenarios.
2. Load `SKILL.md` first.
3. Load only required reference files.
4. Enforce live venue verification from official sources before applying constraints.
5. Enforce citation safety:
   - DOI-first retrieval (`scripts/doi_to_bibtex.py`)
   - explicit placeholders for unresolved references
   - no fabricated citations
6. Use venue checklists before claiming submission readiness.

## Safety-Critical Rules

- Never rely on stale venue policies from memory.
- Never fabricate BibTeX/citations.
- Always map claims to explicit evidence (tables/figures/metrics).
- Always include threats-to-validity coverage.

## Maintenance Protocol

When updating the skill:

1. Edit docs/scripts/assets as needed.
2. Run validation:

```bash
python3 /Users/romel/.codex/skills/skill-creator/scripts/quick_validate.py /Users/romel/.codex/skills/se-paper-writing
```

3. Package distributable artifact:

```bash
python3 /Users/romel/.codex/skills/skill-creator/scripts/package_skill.py /Users/romel/.codex/skills/se-paper-writing /Users/romel/.codex/skills/dist
```

4. Commit and push.

## Scope Reminder

This skill targets:

- Conferences: ICSE, ESEC/FSE, ASE, ISSTA, MSR
- Journals: TSE, TOSEM, EMSE
