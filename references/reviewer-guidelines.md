# Reviewer Guidelines (SE-Focused)

Use this file to self-review drafts before submission and when preparing revisions.

## What reviewers usually evaluate

1. Novelty and contribution clarity
- Is the contribution explicit and non-trivial?
- Is prior work separation clear?

2. Technical soundness
- Are methods reproducible?
- Are assumptions and limitations transparent?

3. Empirical rigor
- Are baselines strong and fair?
- Are statistics and effect sizes reported correctly?
- Are threats to validity addressed?

4. Significance
- Does the result matter to software engineering practice or theory?
- Is the impact likely to transfer?

5. Presentation quality
- Is the narrative coherent?
- Are figures/tables interpretable without excessive context?

## Self-Review Rubric

| Dimension | Failing signal | Passing signal |
| --- | --- | --- |
| Contribution | Contribution appears in middle of paper only | Contribution is obvious in title/abstract/intro |
| Evidence | Claims do not map to experiments | Every claim maps to explicit evidence |
| Baselines | Outdated or weak baselines | Strongest feasible baselines with fair setup |
| Validity | Thin threats section | Concrete threats and mitigation discussion |
| Reproducibility | Missing scripts/config details | Reproduction path documented end-to-end |

## Revision Workflow

1. Build comment matrix:
- reviewer concern
- paper location
- planned response
- evidence needed

2. Prioritize by risk:
- claim-threatening issues first
- clarity and wording next

3. For each resolved concern, add:
- exact textual change
- supporting figure/table change if needed

4. Re-run `checklists.md` before resubmission.

## Rebuttal/Response Style

- acknowledge concern directly
- state what changed (or why not)
- cite exact location of change
- avoid defensive wording
