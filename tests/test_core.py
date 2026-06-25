from pathlib import Path

import pytest

from decision_journal_agent.core import (
    DecisionEntry,
    default_journal_dir,
    record_review,
    render_entry,
    slugify,
    write_entry,
)


def test_slugify():
    assert slugify("Delay launch by two weeks") == "delay-launch-by-two-weeks"


def test_render_entry():
    entry = DecisionEntry(title="Test", confidence=0.8, review_date="2026-05-01")
    out = render_entry(entry)
    assert "# Test" in out
    assert "0.80" in out


def test_entry_validates_confidence_and_review_date():
    with pytest.raises(ValueError, match="confidence"):
        DecisionEntry(title="Test", confidence=1.1, review_date="2026-05-01")
    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        DecisionEntry(title="Test", confidence=0.5, review_date="not-a-date")


def test_default_journal_dir_is_outside_repository_checkout():
    assert default_journal_dir().name == "entries"
    assert ".decision-journal" in str(default_journal_dir())


def test_write_entry_protects_existing_file_by_default(tmp_path):
    entry = DecisionEntry(title="A decision", confidence=0.5, review_date="2026-05-01")
    write_entry(tmp_path, entry)

    with pytest.raises(FileExistsError):
        write_entry(tmp_path, entry)


def test_record_review_updates_supported_entry(tmp_path):
    entry = DecisionEntry(title="A decision", confidence=0.5, review_date="2026-05-01")
    path = write_entry(tmp_path, entry)

    record_review(path, "The fictional outcome met the expected result.", "Use the same review trigger next time.")

    text = Path(path).read_text(encoding="utf-8")
    assert "Reviewed on:" in text
    assert "fictional outcome" in text
    assert "review trigger" in text
