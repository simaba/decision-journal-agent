# Choose a bounded fictional pilot

- Date: 2026-04-01
- Confidence: 0.70
- Review date: 2026-05-01

## Context

A fictional operations team needs to decide whether to test a read-only helper with a small synthetic information set before considering broader use.

## Decision

Run a time-boxed fictional pilot with no write-capable tools and no real data.

## Assumptions

- A synthetic task set is sufficient to test the user journey.
- The pilot can be stopped without affecting any real workflow.

## Success criteria

- Participants can complete a fictional task using cited draft answers.
- No simulated policy or data-boundary hard gate fails.

## Signals to watch

- unresolved source conflicts
- unclear escalation path
- user confusion about whether output is a draft

## Actual outcome

- Reviewed on: 2026-05-01
- Outcome: The fictional pilot met its bounded learning goal, but source-conflict handling needed clearer user wording.

## Lessons learned

Keep pilots read-only, make uncertainty visible, and define the escalation path before expanding scope.
