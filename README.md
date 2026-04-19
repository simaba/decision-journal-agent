# decision-journal-agent

A lightweight forecasting and decision-journaling agent for PM work.

This repo captures decisions with context, assumptions, confidence, review dates, and success criteria, then prompts calibration reviews over time.

## Why it matters

Many teams document decisions but do not revisit them. That makes learning weak and accountability fuzzy.

This repo helps you:

- capture decisions consistently
- record confidence and assumptions
- schedule review points
- compare expected vs actual outcomes
- improve calibration over time

## Features

- markdown-based decision entries
- CLI to create and review decisions
- simple confidence tracking
- review queue generation
- reusable journal template

## Quick start

```bash
pip install -e .
decision-journal new "Delay launch by two weeks" --confidence 0.72 --review-date 2026-05-15
decision-journal due
```

## Repo layout

- `skills/decision-journaling`
- `agents/decision-journaler`
- `templates/decision-entry.md`
- `entries/` for journal files
- `src/` for light CLI logic
