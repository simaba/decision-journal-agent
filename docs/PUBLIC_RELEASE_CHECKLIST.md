# Public Release Checklist

Before making this repository public:

- [ ] Confirm only fictional examples are tracked under `entries/examples/` or `examples/`.
- [ ] Confirm no real entries, private reasoning, personal data, employment information, financial details, health details, relationship information, or confidential work material is present.
- [ ] Review all branches, complete git history, issues, pull requests, comments, Actions logs/artifacts, releases, tags, screenshots, and attachments.
- [ ] Confirm the CLI default remains outside the repository checkout and `.gitignore` is not treated as a privacy guarantee.
- [ ] Run tests and manually exercise `new`, `due`, and `review` using a temporary directory.
- [ ] Check that README, `DATA_PRIVACY.md`, examples, and changelog agree on the public scope.
- [ ] Create a draft release and inspect notes/assets before publishing.

Once sensitive data has been committed or uploaded, making the repository private again does not reliably remove copies or history. Remediation may require history rewriting, credential rotation, or platform support.