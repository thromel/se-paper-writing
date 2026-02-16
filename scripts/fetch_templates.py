#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


REQUIRED_KEYS = {"venue", "publisher", "landing_url", "template_url", "notes"}
DEFAULT_UA = "Mozilla/5.0 (compatible; se-paper-writing/1.0)"


def load_manifest(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Manifest must be a JSON array.")
    rows: list[dict[str, str]] = []
    for idx, raw in enumerate(data, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"Row {idx} is not an object.")
        missing = REQUIRED_KEYS - set(raw.keys())
        if missing:
            missing_str = ", ".join(sorted(missing))
            raise ValueError(f"Row {idx} missing keys: {missing_str}")
        row: dict[str, str] = {}
        for key in REQUIRED_KEYS:
            value = raw[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Row {idx} key '{key}' must be a non-empty string.")
            row[key] = value.strip()
        rows.append(row)
    return rows


def pick_rows(rows: list[dict[str, str]], venue: str | None, select_all: bool) -> list[dict[str, str]]:
    if select_all:
        return rows

    assert venue is not None
    target = venue.strip().lower()
    selected = [row for row in rows if row["venue"].lower() == target]
    if not selected:
        known = ", ".join(sorted({row["venue"] for row in rows}))
        raise KeyError(f"Unknown venue '{venue}'. Valid venues: {known}")
    return selected


def infer_filename(template_url: str, content_type: str, venue: str) -> str:
    parsed = urlparse(template_url)
    candidate = Path(parsed.path).name
    if not candidate:
        candidate = f"{venue}.download"

    suffix = Path(candidate).suffix.lower()
    if suffix:
        return candidate

    lowered = content_type.lower()
    if "html" in lowered:
        return candidate + ".html"
    if "json" in lowered:
        return candidate + ".json"
    if "xml" in lowered:
        return candidate + ".xml"
    return candidate + ".bin"


def download_bytes(url: str) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": DEFAULT_UA})
    with urlopen(req, timeout=60) as resp:
        data = resp.read()
        content_type = resp.headers.get("Content-Type", "")
    return data, content_type


def write_metadata(out_dir: Path, row: dict[str, str], status: str, output_file: str | None) -> None:
    metadata = {
        "venue": row["venue"],
        "publisher": row["publisher"],
        "landing_url": row["landing_url"],
        "template_url": row["template_url"],
        "notes": row["notes"],
        "status": status,
        "output_file": output_file,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    meta_path = out_dir / "source.json"
    meta_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def handle_row(row: dict[str, str], dest_root: Path, dry_run: bool, force: bool) -> bool:
    venue = row["venue"]
    out_dir = dest_root / venue
    template_url = row["template_url"]

    if dry_run:
        print(f"[dry-run] venue={venue}")
        print(f"[dry-run]  landing:  {row['landing_url']}")
        print(f"[dry-run]  template: {template_url}")
        print(f"[dry-run]  out dir:  {out_dir}")
        return True

    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        data, content_type = download_bytes(template_url)
    except HTTPError as err:
        print(f"[error] {venue}: HTTP {err.code} for {template_url}", file=sys.stderr)
        write_metadata(out_dir, row, f"http_error_{err.code}", None)
        return False
    except URLError as err:
        print(f"[error] {venue}: URL error for {template_url}: {err}", file=sys.stderr)
        write_metadata(out_dir, row, "url_error", None)
        return False
    except TimeoutError:
        print(f"[error] {venue}: timeout for {template_url}", file=sys.stderr)
        write_metadata(out_dir, row, "timeout", None)
        return False

    filename = infer_filename(template_url, content_type, venue)
    out_file = out_dir / filename

    if out_file.exists() and not force:
        print(f"[skip] {venue}: {out_file} exists (use --force to overwrite)")
        write_metadata(out_dir, row, "skipped_exists", str(out_file))
        return True

    out_file.write_bytes(data)
    print(f"[ok] {venue}: wrote {out_file}")
    write_metadata(out_dir, row, "downloaded", str(out_file))
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch SE-paper template resources from template-sources.json."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--venue", help="Venue id from template-sources.json (e.g., icse)")
    group.add_argument("--all", action="store_true", help="Fetch all venue entries")
    parser.add_argument("--dest", default="./se_templates", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned downloads only")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args(argv)

    manifest_path = Path(__file__).resolve().parent.parent / "references" / "template-sources.json"
    try:
        rows = load_manifest(manifest_path)
    except Exception as err:
        print(f"[error] could not load manifest: {err}", file=sys.stderr)
        return 1

    try:
        selected = pick_rows(rows, args.venue, args.all)
    except KeyError as err:
        print(f"[error] {err}", file=sys.stderr)
        return 2

    dest_root = Path(args.dest).resolve()
    if not args.dry_run:
        dest_root.mkdir(parents=True, exist_ok=True)

    ok = True
    for row in selected:
        ok = handle_row(row, dest_root, args.dry_run, args.force) and ok

    return 0 if ok else 3


if __name__ == "__main__":
    raise SystemExit(main())
