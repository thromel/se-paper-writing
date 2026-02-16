#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DOI_PATTERN = re.compile(r"^10\.\S+/\S+$")


def normalize_doi(raw: str) -> str:
    doi = raw.strip()
    doi = doi.removeprefix("https://doi.org/")
    doi = doi.removeprefix("http://doi.org/")
    doi = doi.removeprefix("doi:")
    return doi.strip()


def fetch_bibtex(doi: str) -> str:
    url = f"https://doi.org/{quote(doi, safe='/')}"
    req = Request(
        url,
        headers={
            "Accept": "application/x-bibtex",
            "User-Agent": "Mozilla/5.0 (compatible; se-paper-writing/1.0)",
        },
    )
    with urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch verified BibTeX entry from DOI.")
    parser.add_argument("--doi", help="DOI value (can omit and provide via stdin).")
    args = parser.parse_args(argv)

    raw = args.doi if args.doi is not None else sys.stdin.read()
    doi = normalize_doi(raw)
    if not doi:
        print("[error] missing DOI. Provide --doi or stdin.", file=sys.stderr)
        return 2
    if not DOI_PATTERN.match(doi):
        print(f"[error] invalid DOI format: '{doi}'", file=sys.stderr)
        return 2

    try:
        bibtex = fetch_bibtex(doi)
    except HTTPError as err:
        print(f"[error] DOI lookup failed with HTTP {err.code} for {doi}", file=sys.stderr)
        return 3
    except URLError as err:
        print(f"[error] DOI lookup network failure for {doi}: {err}", file=sys.stderr)
        return 3
    except TimeoutError:
        print(f"[error] DOI lookup timed out for {doi}", file=sys.stderr)
        return 3

    if not bibtex.strip():
        print(f"[error] empty BibTeX response for {doi}", file=sys.stderr)
        return 3

    sys.stdout.write(bibtex.rstrip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
