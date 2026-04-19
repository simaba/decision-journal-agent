from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date
from .core import DecisionEntry, write_entry


def main() -> int:
    parser = argparse.ArgumentParser(prog="decision-journal")
    sub = parser.add_subparsers(dest="command")

    new = sub.add_parser("new")
    new.add_argument("title")
    new.add_argument("--confidence", type=float, required=True)
    new.add_argument("--review-date", required=True)
    new.add_argument("--dir", default="entries")

    due = sub.add_parser("due")
    due.add_argument("--dir", default="entries")

    args = parser.parse_args()

    if args.command == "new":
        entry = DecisionEntry(title=args.title, confidence=args.confidence, review_date=args.review_date)
        path = write_entry(args.dir, entry)
        print(path)
        return 0

    if args.command == "due":
        today = date.today().isoformat()
        base = Path(args.dir)
        if not base.exists():
            return 0
        for path in sorted(base.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            marker = "- Review date: "
            if marker in text:
                review = text.split(marker, 1)[1].splitlines()[0].strip()
                if review <= today:
                    print(path)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
