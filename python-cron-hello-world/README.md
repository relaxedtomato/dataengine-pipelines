# python-cron-hello-world

> **Note:** This example is a work in progress and may be incomplete.

## Overview

A hello world serverless function triggered on a cron schedule. Logs a greeting and environment variables on each invocation.

| | |
|---|---|
| **Trigger** | Cron |
| **Runtime** | Python 3.11 |
| **Status** | In Progress |

## Prerequisites

- Access to a VAST DataEngine instance
- A configured pipeline with a cron trigger
- `vastde` CLI installed and configured — see [DEVELOPMENT.md](../DEVELOPMENT.md)

## Configuration

Copy `config.example.yaml` to `config.yaml` and fill in your values:

```bash
cp config.example.yaml config.yaml
```

### Environment Variables

| Variable | Type | Description |
|---|---|---|
| `GREETING` | env | Message logged on each invocation |
| `LOG_LEVEL` | env | Logging verbosity |

Never commit `config.yaml` — it is gitignored.

## Run Function on DataEngine

Follow these steps to deploy and run the function on DataEngine. For detailed instructions, refer to the [DataEngine Documentation](https://kb.vastdata.com/documentation/docs/version-54-3).

### 1. Build Function

Build and push the image to your container registry, then register it as a function in DataEngine via the UI or CLI.

### 2. Set up Trigger

Create a cron trigger via the DataEngine UI or CLI.

### 3. Deploy Pipeline

Create a pipeline connecting the trigger to the function and deploy via the DataEngine UI or CLI.

```bash
vastde logs tail <pipeline> --function hello-world
```

## Local Development

### Build

```bash
vastde functions build hello-world
```

### Run locally

```bash
vastde functions localrun hello-world -c config.yaml
```

### Invoke

```bash
vastde functions invoke --generate-event --url http://localhost:8080/
```

## Resources

- [DEVELOPMENT.md](../DEVELOPMENT.md) — local setup and CLI workflow
- [CONTRIBUTING.md](../CONTRIBUTING.md) — how to contribute
- [DataEngine Docs](https://kb.vastdata.com/documentation/docs/version-54-3)
- [DataEngine CLI](https://github.com/vast-data/dataengine-cli)
- [VAST Community](https://community.vastdata.com/)
- [VAST Developers](https://www.vastdata.com/developers)
