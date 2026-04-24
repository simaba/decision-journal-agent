# decision-journal-agent

A lightweight decision-journal tool for PM and operator workflows.

## Status

**Early working CLI.**

This repository already supports creating markdown decision entries and listing entries whose review date is due. It does **not** yet provide full calibration analytics, expected-vs-actual scoring, or advanced review workflows.

## What it is for

Use this repo when you want a small, local workflow for:

- capturing a decision consistently
- recording confidence at the time of the decision
- assigning a review date
- maintaining a simple queue of decisions that need review

## What it does today

- creates markdown-based decision entries
- stores confidence and review date in each entry
- provides a `due` command to list entries ready for review
- uses a reusable journal template

## What it does not claim yet

This repo does **not** yet claim:

- calibration scoring over time
- expected-vs-actual variance analysis
- forecasting metrics dashboards
- automated review summaries
- statistical quality measurement for decision quality

## Quick start

```bash
pip install -e .
decision-journal new "Delay launch by two weeks" --confidence 0.72 --review-date 2026-05-15
decision-journal due
```

## Repo layout

- `templates/decision-entry.md`
- `entries/` for journal files
- `src/` for lightweight CLI logic
- `skills/decision-journaling`
- `agents/decision-journaler`

## Next maturity step

To justify stronger decision-quality claims, this repo should next add:

1. a `review` command for recording actual outcomes
2. structured comparison between expected and actual results
3. simple calibration summaries over time
4. tests for entry parsing and review workflows

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*