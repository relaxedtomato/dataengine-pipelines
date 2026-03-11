# Contributing to VAST DataEngine Serverless Functions

Thanks for taking the time to contribute! Whether you're fixing a bug, adding a new function, or improving docs, we appreciate it. 🎉

## Ways to contribute

- **Report a bug** open an issue with the `bug` label
- **Propose a new function** open an issue with the `function-idea` label
- **Improve docs** open a PR directly for small fixes
- **Submit a function** follow the steps below

## Before you start

For new functions or significant changes, open an issue first so we can align before you write code. For typo fixes and small doc changes, a PR directly is fine.

## Branching

All branches target `main` directly. Never commit to `main` directly — always work on a branch and open a PR.

| Type | Format | Example |
|---|---|---|
| New function | `feature/<name>` | `feature/python-event-hello-world` |
| Bug fix | `fix/<name>` | `fix/cron-timeout` |
| Docs | `docs/<name>` | `docs/update-readme` |

## Commit message format

```
feat(python-event-hello-world): add s3 upload handler
fix(python-cron-hello-world): handle missing context
docs(readme): update quick start section
```

## PR checklist ✅

Before opening a PR, make sure:

- [ ] Your branch is up to date with `main`
- [ ] `main.py` defines both `init()` and `handler()`
- [ ] An entry has been added to `registry.json`
- [ ] Your function folder has a `README.md` that includes step-by-step instructions to deploy and run the function (the happy path)
- [ ] The serverless function has been tested end to end on DataEngine with no build or runtime errors when following the happy path
- [ ] (optional, but recommended) Tests pass locally (i.e. `pytest tests/`)
