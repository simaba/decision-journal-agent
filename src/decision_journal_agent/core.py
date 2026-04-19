from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from datetime import date


@dataclass
class DecisionEntry:
    title: str
    confidence: float
    review_date: str


def slugify(text: str) -> str:
    return "-".join("".join(c.lower() if c.isalnum() else " " for c in text).split())


def render_entry(entry: DecisionEntry) -> str:
    today = date.today().isoformat()
    return f"""# {entry.title}

- Date: {today}
- Confidence: {entry.confidence:.2f}
- Review date: {entry.review_date}

## Context

## Decision

## Assumptions

## Success criteria

## Signals to watch

## Actual outcome

## Lessons learned
"""


def write_entry(base_dir: str | Path, entry: DecisionEntry) -> Path:
    base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / f"{slugify(entry.title)}.md"
    path.write_text(render_entry(entry), encoding="utf-8")
    return path
