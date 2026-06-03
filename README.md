# Decision Journal Agent

A lightweight decision-journal tool for PM, product, strategy, and operator workflows.

## Maturity

**Early working CLI.**

This repository supports creating Markdown decision entries and listing entries whose review date is due. It does not yet provide calibration analytics, expected-versus-actual scoring, or advanced review workflows.

## Purpose

Decision journals help teams and individuals improve decision quality by recording what was decided, why it was decided, how confident the decision-maker was, and when the outcome should be reviewed.

This repository provides a small local workflow for:

- capturing decisions consistently
- recording confidence at the time of decision
- assigning a review date
- maintaining a simple queue of decisions due for review
- supporting reflection after outcomes are known

## Current capabilities

- creates Markdown-based decision entries
- stores confidence and review date in each entry
- provides a `due` command to list entries ready for review
- uses a reusable journal template

## Quick start

```bash
pip install -e .
decision-journal new "Delay launch by two weeks" --confidence 0.72 --review-date 2026-05-15
decision-journal due
```

## Repository layout

```text
templates/decision-entry.md   reusable entry template
entries/examples/             fictional examples safe to publish
src/                          lightweight CLI logic
skills/decision-journaling    reusable decision-journaling skill
agents/decision-journaler     agent instructions for decision capture and review
```

## Publication safety

Decision journals can contain sensitive business, career, financial, health, relationship, or personal information. If this repository is public or shared, do not commit real decision entries.

Recommended pattern:

- keep real entries outside the repository
- use `entries/examples/` only for fictional examples
- avoid naming real employers, customers, partners, vendors, colleagues, or confidential projects
- remove private reasoning, negotiation details, and internal risk assessments before sharing

## Out of scope

This early CLI does not yet provide:

- calibration scoring over time
- expected-versus-actual variance analysis
- forecasting metrics dashboards
- automated review summaries
- statistical quality measurement for decision quality

## Roadmap

To support stronger decision-quality analysis, this repository should add:

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
