---
name: se-paper-writing
description: Use when drafting, revising, or submitting software engineering research papers for ICSE, ESEC/FSE, ASE, ISSTA, MSR, TSE, TOSEM, or EMSE, especially when turning repository results into a manuscript, selecting venue-specific structure, verifying citations, or preparing submission and camera-ready packages.
---

# SE Paper Writing

## Overview

Write software engineering papers as a claim-evidence story with venue-aware packaging, reproducibility discipline, and strict citation verification. Use this skill to move from code and experiment artifacts to a submission-ready manuscript.

## Quick Start

1. Choose venue and track.
2. Open official instructions from `references/sources.md`.
3. Verify current author policies before applying any page-limit or formatting rule.
4. Build the claim-evidence matrix from `references/evaluation-playbook.md`.
5. Start from `assets/se_skeleton/` and draft sections.
6. Use `references/checklists.md` before submission.

## Mandatory Rules

### Live venue verification is required

Never trust cached or memory-based venue limits, anonymity rules, or artifact requirements. Always verify from official sources in the current session and cite the date checked in your notes.

### Never hallucinate citations

Never fabricate references, DOIs, or BibTeX. Fetch citations via DOI and verify claims before citing.

If verification fails, emit an explicit placeholder:

```latex
% VERIFY BEFORE SUBMISSION
\cite{PLACEHOLDER_verify_source} % TODO: unresolved citation
```

## Workflow

1. Classify the paper type.
Conference paper flow: ICSE, ESEC/FSE, ASE, ISSTA, MSR.
Journal flow: TSE, TOSEM, EMSE.
2. Use `references/venue-playbook.md` to choose structure and template family.
3. Build the RQ-to-claim matrix and evidence plan with `references/evaluation-playbook.md`.
4. Draft sections and tables using `assets/se_skeleton/`.
5. Build references using `scripts/doi_to_bibtex.py` and the process in `references/citation-workflow.md`.
6. Run final venue-specific checklist in `references/checklists.md`.
7. For template retrieval, run `scripts/fetch_templates.py` and review notes in `references/template-sources.json`.

## Conference vs Journal Routing

- Conference priorities: novelty positioning, concise methods, compact but complete empirical evidence.
- Journal priorities: deeper methodology detail, extended threats-to-validity discussion, broader and more stable empirical support.
- For resubmission (conference to journal), expand rationale, add robustness analyses, and re-check all policy constraints from official pages.

## Tools

- `scripts/fetch_templates.py`
Download venue template resources from `references/template-sources.json`.
Use `--venue <id>` or `--all`, and optionally `--dry-run` to inspect planned downloads.
- `scripts/doi_to_bibtex.py`
Fetch verified BibTeX from DOI endpoint. Never replace failures with guessed entries.

## References to Load on Demand

- `references/venue-playbook.md`
Venue routing, policy verification workflow, and conversion guidance.
- `references/evaluation-playbook.md`
Claim-evidence matrix, RQ mapping, statistical expectations, threats to validity.
- `references/reviewer-guidelines.md`
Reviewer criteria and revision/rebuttal workflow.
- `references/checklists.md`
Submission and camera-ready checklists for conference and journal flows.
- `references/citation-workflow.md`
Citation verification workflow and failure-handling patterns.
- `references/sources.md`
Official source registry for venue and publisher pages.
- `references/template-sources.json`
Machine-readable template source manifest consumed by `fetch_templates.py`.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Applying remembered page limits | Verify current instructions from official sources in-session. |
| Writing prose before evidence plan | Freeze claim-evidence matrix first. |
| Reporting p-values only | Report effect sizes and confidence intervals. |
| Weak threats-to-validity section | Cover construct, internal, external, and conclusion validity explicitly. |
| Guessing citations | Use DOI workflow and mark unresolved citations as placeholders. |

## Minimal Deliverable Standard

Before claiming submission-ready quality:
- venue policy verified from official source in current session
- claims linked to explicit evidence tables/figures
- citation list fully verified or explicitly marked placeholders
- checklist completed for the selected venue type
