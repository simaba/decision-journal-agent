from __future__ import annotations

import argparse
from pathlib import Path

from .core import (
    DecisionEntry,
    default_journal_dir,
    due_entries,
    invalid_review_date_entries,
    record_review,
    slugify,
    write_entry,
)


def _journal_dir(value: str | None) -> Path:
    return Path(value).expanduser() if value else default_journal_dir()


def main() -> int:
    parser = argparse.ArgumentParser(prog="decision-journal")
    sub = parser.add_subparsers(dest="command")

    new = sub.add_parser("new")
    new.add_argument("title")
    new.add_argument("--confidence", type=float, required=True)
    new.add_argument("--review-date", required=True)
    new.add_argument(
        "--dir",
        help="Journal directory. Defaults to ~/.decision-journal/entries outside this repository.",
    )
    new.add_argument("--overwrite", action="store_true")

    due = sub.add_parser("due")
    due.add_argument(
        "--dir",
        help="Journal directory. Defaults to ~/.decision-journal/entries outside this repository.",
    )
    due.add_argument(
        "--include-reviewed",
        action="store_true",
        help="Include entries that already contain a recorded review.",
    )

    review = sub.add_parser("review")
    review.add_argument("title")
    review.add_argument("--outcome", required=True)
    review.add_argument("--lessons", required=True)
    review.add_argument(
        "--dir",
        help="Journal directory. Defaults to ~/.decision-journal/entries outside this repository.",
    )

    args = parser.parse_args()

    try:
        if args.command == "new":
            entry = DecisionEntry(
                title=args.title,
                confidence=args.confidence,
                review_date=args.review_date,
            )
            path = write_entry(
                _journal_dir(args.dir),
                entry,
                overwrite=args.overwrite,
            )
            print(path)
            return 0

        if args.command == "due":
            base = _journal_dir(args.dir)
            for path in due_entries(base, include_reviewed=args.include_reviewed):
                print(path)
            for path in invalid_review_date_entries(base):
                print(f"Skipping invalid review date in {path}", flush=True)
            return 0

        if args.command == "review":
            path = _journal_dir(args.dir) / f"{slugify(args.title)}.md"
            print(record_review(path, args.outcome, args.lessons))
            return 0
    except (FileExistsError, OSError, ValueError) as exc:
        parser.error(str(exc))

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
