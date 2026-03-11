# VAST DataEngine Serverless Functions

## What is VAST DataEngine?

[VAST DataEngine](https://www.vastdata.com/platform/dataengine) is a serverless computing platform built into the VAST [AI Operating System](https://www.vastdata.com/platform/ai-os). It lets you build, deploy, and scale data processing functions without managing infrastructure, running compute directly where data lives to eliminate costly data movement and duplication. The platform handles scheduling, event detection, and resource allocation so you can focus on business logic. At its core, DataEngine gives you three building blocks:

- **Functions:** Your code built into container images and executed on VAST compute nodes (cnodes)
- **Triggers:** Event sources like S3 uploads or cron schedules
- **Pipelines:** Orchestration layer that connects triggers to functions

For a full overview, check out our recent blog post: [VAST DataEngine: Bringing Compute to Your Data](https://www.vastdata.com/blog/vast-dataengine-bringing-compute-to-your-data)

---

## What's in this repo?

| Function | Trigger | Runtime | Status |
|---|---|---|---|
| [python-event-hello-world](functions/python-event-hello-world/) | Event (S3 upload) | Python 3.11 | coming soon |

> This table is generated from [`registry.json`](registry.json). Do not edit it manually.

---

## Quick Start

Browse the [functions](functions/) folder, pick one, and follow the README inside it.

---

## How to add a new function

1. (Optional, but recommended) Copy the relevant template from [`_serverless_templates/`](_serverless_templates/) into `functions/your-function-name/`
2. Implement `init()` and `handler()` in `main.py`
3. Add an entry to [`registry.json`](registry.json) and open a PR against the `develop` branch

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow and PR checklist.

---

## Folder layout

```
serverless-functions/
├── python-event-hello-world/       # Each function is a self-contained folder
├── python-event-starter/           # Reference scaffold, kept in sync with vastde CLI
├── scripts/
│   └── validate_function.py        # Checks a function folder has all required files
└── registry.json                   # Machine-readable index of all functions
```

> Each function folder is fully self-contained — all dependencies, helpers, and tests live inside it.

