# Decision Journal Agent

A lightweight decision-journal tool for PM, product, strategy, and operator workflows.

## Status

**Early working CLI.**

This repository supports creating markdown decision entries and listing entries whose review date is due. It does **not** yet provide full calibration analytics, expected-vs-actual scoring, or advanced review workflows.

## What it is for

Use this repo when you want a small, local workflow for:

- capturing a decision consistently
- recording confidence at the time of the decision
- assigning a review date
- maintaining a simple queue of decisions that need review
- improving decision quality through later reflection

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

## Public-use safety note

Decision journals can easily contain sensitive business, career, financial, health, relationship, or personal information. If you use this repository in a public or shared GitHub repo, do not commit real decision entries.

Recommended public-safe pattern:

- keep real entries outside the repository
- use `entries/examples/` only for fictional examples
- avoid naming real employers, customers, partners, vendors, colleagues, or confidential projects
- remove private reasoning, negotiation details, and internal risk assessments before sharing

## Quick start

```bash
pip install -e .
decision-journal new "Delay launch by two weeks" --confidence 0.72 --review-date 2026-05-15
decision-journal due
```

## Repo layout

```text
templates/decision-entry.md   # reusable entry template
entries/examples/             # fictional examples safe to publish
src/                          # lightweight CLI logic
skills/decision-journaling    # reusable decision-journaling skill
agents/decision-journaler     # agent instructions for decision capture and review
```

## Next maturity step

To justify stronger decision-quality claims, this repo should next add:

1. a `review` command for recording actual outcomes
2. structured comparison between expected and actual results
3. simple calibration summaries over time
4. tests for entry parsing and review workflows
5. public-safe fictional examples showing the full lifecycle from decision to review

## Scope and disclaimer

This repository is shared in a personal capacity. It is not legal, financial, medical, employment, or psychological advice. It is not a substitute for professional judgment, qualified review, or formal organizational decision processes.

AI-generated decision summaries should be treated as drafts. Validate facts, assumptions, risks, constraints, and outcomes before using them for important decisions.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
