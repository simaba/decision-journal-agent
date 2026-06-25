# Data and Privacy Boundaries

Decision journals often contain sensitive business, career, financial, health, relationship, or personal material. Treat real entries as private personal data.

## Safe default

The CLI now writes new entries to `~/.decision-journal/entries` unless `--dir` is explicitly supplied. This keeps real journals outside the repository checkout by default.

## Public repository policy

Only `entries/examples/` and `examples/` may contain entries intended for public sharing. Those entries must be fictional or fully sanitized.

Never commit:

- real employer, customer, partner, vendor, colleague, or project names
- commercial, legal, employment, financial, health, relationship, or personal details
- internal decisions, negotiations, risks, performance information, or roadmap details
- credentials, links to private systems, attachments, or evidence files
- private reasoning that another person did not consent to share

## Before publishing

1. Inspect the current worktree and all branches.
2. Inspect commit history, pull requests, issues, Actions logs, artifacts, and attachments.
3. Confirm ignored directories did not previously contain tracked files.
4. Keep real entries in the default local directory or another private location.
5. Publish only fictional lifecycle examples.

The `.gitignore` file is a convenience, not a privacy control. Once private content is committed or uploaded, it may require history rewriting, credential rotation, or platform support to remove it safely.