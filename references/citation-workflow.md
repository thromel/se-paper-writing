# Citation Workflow

This workflow prevents citation hallucination.

## Rules

1. Never write BibTeX from memory.
2. Prefer DOI-based retrieval.
3. If unresolved, mark placeholder and report it explicitly.

## DOI-First Workflow

1. Search for candidate paper and verify it exists.
2. Resolve DOI from official metadata source.
3. Run:

```bash
python3 scripts/doi_to_bibtex.py --doi 10.xxxx/xxxxx
```

4. Insert returned BibTeX entry.
5. Confirm cited claim is actually supported by the paper.

## Unknown/Unverified Citation Handling

Use explicit placeholder if verification fails:

```latex
\cite{PLACEHOLDER_verify_source}
```

And include a note:

```text
Citation unresolved: [title or claim], verification required before submission.
```

## Quality Checks

- DOI resolves successfully.
- BibTeX entry is non-empty.
- Authors/title/year align with intended citation.
- Claim and citation semantics match.
