# Evaluation Playbook

Design experiments so each claim has clear evidence and clear limits.

## Claim-Evidence Matrix (Create before prose)

For each claim, define:
- claim text (one sentence)
- research question (RQ id)
- primary metric(s)
- comparison baseline(s)
- expected failure mode
- required table/figure id

Minimum matrix columns:

| Claim | RQ | Metric | Baselines | Dataset/Subjects | Statistical plan | Figure/Table |
| --- | --- | --- | --- | --- | --- | --- |

## RQ to Evidence Mapping

| RQ Type | Typical evidence |
| --- | --- |
| Effectiveness | Accuracy/quality gains, defect detection lift, success rate, or task completion benefit |
| Efficiency | Runtime, memory, token cost, engineering cost, or throughput |
| Robustness | Sensitivity tests, cross-project transfer, noise/shift tests |
| Human factors | User study outcomes, task time, subjective workload/confidence |
| Generalizability | Multiple ecosystems, languages, projects, or domains |

## Statistical Reporting Baseline

Always report:
- sample size and unit of analysis
- confidence intervals
- effect sizes (not just p-values)
- exact test used and assumptions
- multiple-comparison correction if many hypotheses are tested

Prefer:
- bootstrap confidence intervals for unstable distributions
- non-parametric tests when normality assumptions are weak
- practical significance discussion (engineering relevance)

## Threats to Validity Structure

Every SE paper should include explicit coverage of:
- Construct validity: does metric represent the intended concept?
- Internal validity: could confounders explain the effect?
- External validity: does result transfer beyond sampled projects/tasks?
- Conclusion validity: are inference methods statistically sound?

## Reproducibility Expectations

Include at least:
- environment and dependency lock details
- scripts for every figure/table
- random seed policy
- dataset versioning and filtering logic
- failure-case catalog

## Common Evidence Gaps

| Gap | Fix |
| --- | --- |
| Strong metric gain but no cost accounting | Add runtime/cost/latency table and trade-off discussion |
| One benchmark only | Add cross-project or cross-dataset evaluation |
| No ablations | Remove one mechanism at a time and quantify change |
| No failure analysis | Include representative failure modes and mitigations |
