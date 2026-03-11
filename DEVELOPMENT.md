# Development Guide

## Prerequisites

Before you get started, make sure you have the following installed:

- Python 3.11+
- Docker (required for building functions)
- `vastde` CLI — see install steps below

## Install the CLI

Download the latest binary for your platform from the [DataEngine CLI releases page](https://github.com/vast-data/dataengine-cli/releases), then:

```bash
# macOS / Linux
chmod +x vastde
mv vastde /usr/local/bin/vastde

# Verify
vastde --version
```

Then initialise your credentials:

```bash
vastde config init
```

This creates `~/.vast/config.toml` with your VMS endpoint and credentials. Never commit this file.

## Scaffold a new function

```bash
vastde functions init python-pip <your-function-name>
```

This generates:

```
<your-function-name>/
├── main.py          # Handler entry point (init and handler)
├── requirements.txt # Python dependencies
├── Aptfile          # System packages
├── customDeps       # Custom/private shared libraries
└── README.md        # Generated development guide
```

## Build

```bash
vastde functions build <function-name>
```

Docker must be running. The build will:
- Install system packages from `Aptfile`
- Install Python dependencies from `requirements.txt`
- Install custom dependencies from `customDeps`
- Create a container image ready for deployment

## Test locally

```bash
# Basic local run
vastde functions localrun <function-name>

# Run with custom port
vastde functions localrun <function-name> --port 9090

# Run with config
vastde functions localrun <function-name> -c config.yaml
```

Invoke your function with an auto-generated event:

```bash
vastde functions invoke --generate-event --url http://localhost:8080/  # change port if specified via --port
```

Alternatively, create a `cloudevent.yaml` in your function folder to send a custom event specific to your function, then invoke with:

```bash
vastde functions invoke <function-name> -f cloudevent.yaml
```

## Configuration

Create a `config.yaml` to pass environment variables and secrets to your function:

```yaml
envs:
  MY_VARIABLE: "hello-world"

secrets:
  username: "myuser"
  password: "mypassword"
```

Never commit real credentials. `config.yaml` is in `.gitignore` — use placeholder values and document what each variable does in your function's `README.md`.

## Deploy

Deploy via the DataEngine UI or CLI. See the per-function `README.md` for function-specific steps.

## Logs

```bash
vastde logs tail <pipeline> --function <your-function-name>
```

## Run unit tests (optional)

```bash
pytest tests/
```
