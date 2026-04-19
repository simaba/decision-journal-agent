from decision_journal_agent.core import slugify, DecisionEntry, render_entry


def test_slugify():
    assert slugify("Delay launch by two weeks") == "delay-launch-by-two-weeks"


def test_render_entry():
    entry = DecisionEntry(title="Test", confidence=0.8, review_date="2026-05-01")
    out = render_entry(entry)
    assert "# Test" in out
    assert "0.80" in out
