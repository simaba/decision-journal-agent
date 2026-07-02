from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


DEFAULT_JOURNAL_DIR = Path.home() / ".decision-journal" / "entries"


@dataclass
class DecisionEntry:
    title: str
    confidence: float
    review_date: str

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("title must not be empty")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        try:
            date.fromisoformat(self.review_date)
        except ValueError as exc:
            raise ValueError("review_date must use YYYY-MM-DD") from exc


def default_journal_dir() -> Path:
    """Return a personal directory outside the repository checkout."""
    return DEFAULT_JOURNAL_DIR


def slugify(text: str) -> str:
    return "-".join("".join(char.lower() if char.isalnum() else " " for char in text).split())


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


def write_entry(
    base_dir: str | Path,
    entry: DecisionEntry,
    *,
    overwrite: bool = False,
) -> Path:
    base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / f"{slugify(entry.title)}.md"
    if path.exists() and not overwrite:
        raise FileExistsError(
            f"{path} already exists; choose a different title or pass --overwrite"
        )
    path.write_text(render_entry(entry), encoding="utf-8")
    return path


def record_review(entry_path: str | Path, outcome: str, lessons: str) -> Path:
    """Record a dated outcome and lesson for an existing journal entry."""
    path = Path(entry_path)
    text = path.read_text(encoding="utf-8")
    if "## Actual outcome\n" not in text or "## Lessons learned\n" not in text:
        raise ValueError("entry does not match the supported decision-journal template")
    if "- Reviewed on:" in text:
        raise ValueError("entry already contains a recorded review")

    reviewed_on = date.today().isoformat()
    outcome_section = "## Actual outcome\n\n- Reviewed on: {}\n- Outcome: {}\n".format(
        reviewed_on,
        outcome.strip(),
    )
    lessons_section = "## Lessons learned\n\n{}\n".format(lessons.strip())
    text = text.replace("## Actual outcome\n", outcome_section, 1)
    text = text.replace("## Lessons learned\n", lessons_section, 1)
    path.write_text(text, encoding="utf-8")
    return path
