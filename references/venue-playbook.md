# Venue Playbook

Use this file to choose workflow and policy checks for software engineering venues.

## Non-Negotiable Rule

Before writing or packaging for any venue:
1. Open the official venue page from `sources.md`.
2. Confirm current requirements in-session (date checked, track, page budget, anonymity policy, artifact policy, camera-ready requirements).
3. Record what was verified and when.

Never reuse year-specific limits from memory.

## Venue Routing Table

| Venue | Type | Typical publisher/template family | Verify first |
| --- | --- | --- | --- |
| ICSE | Conference | ACM (`acmart`) | Track page budget, anonymization, supplementary material rules |
| ESEC/FSE | Conference | ACM (`acmart`) | Track limits, artifact process, rebuttal timeline |
| ASE | Conference | IEEE (`IEEEtran`) | Track format, double-blind policy, appendix handling |
| ISSTA | Conference | ACM (`acmart`) | Artifact process, anonymity, statistical reporting |
| MSR | Conference | ACM or IEEE, track dependent | Short/full paper requirements and replication package expectations |
| TSE | Journal | IEEE journal format | Journal submission rules, replication package expectations |
| TOSEM | Journal | ACM journal format | Journal template choice, disclosure, artifact links |
| EMSE | Journal | Springer journal format | Journal formatting package and required metadata |

## Conference Flow

1. Lock one-sentence claim and 3-5 contribution bullets.
2. Map each contribution to a concrete result table or figure.
3. Keep methods concise; move setup details to appendix/supplement as policy allows.
4. Run conference section of `checklists.md`.

## Journal Flow

1. Keep one-sentence claim, but expand method rationale and assumptions.
2. Add broader robustness studies and deeper threats-to-validity analysis.
3. Expand related work for longitudinal context.
4. Run journal section of `checklists.md`.

## Conversion Workflow (Conference to Journal)

1. Keep central claim and rename contributions for journal framing.
2. Add new experiments that answer reviewer-risk concerns:
   - robustness under realistic variation
   - negative/failure cases
   - practical significance and cost discussion
3. Expand reproducibility details (exact scripts, datasets, environment, seeds).
4. Re-verify all policy details from current official journal instructions.

## Conversion Workflow (Journal to Conference)

1. Compress to one primary technical narrative.
2. Keep only experiments that directly support main claims.
3. Move secondary details to appendix/supplement if allowed.
4. Re-check anonymity and supplementary material requirements.
