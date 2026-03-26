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
  - run `vastde --version` to check installation
  - run `vastde functions list` to check that you have DataEngine access

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
| `myuser` | secrets | username secret |
| `mypassword` | secrets | user password |

Never commit `config.yaml` — it is gitignored.

## Run Function on DataEngine

Follow these steps to deploy and run the function on DataEngine. For detailed instructions, refer to the [DataEngine Documentation](https://kb.vastdata.com/documentation/docs/version-54-3).

All instructions are given using the `vastde` CLI, you can also complete all of them via the DataEngine UI.

### 1. Build Function

Build the function image, then register it as a function in DataEngine:

```sh
# commands
cd python-cron-hello-world
vastde functions build hello-world
```

```sh
# vastde functions build output
Detected language: python
Validating Python version 3.12.*...
Python version 3.12.* resolved to 3.12.12
Building hello-world:latest
App Path: .../python-cron-hello-world
Handlers File: main.py
Build log: .../python-cron-hello-world/build.log
2026/03/18 14:22:18 [Started] Python Builder: hello-world:latest
2026/03/18 14:22:34 [Completed] Python Builder: hello-world:latest
Build completed: hello-world:latest
Build log saved to: .../python-cron-hello-world/build.log
```

Push the image to your container registry that is configured on DataEngine tenant (search for `Container Registries` in VMS):

```sh
docker tag hello-world:latest <registry-host>/<registry-user>/hello-world:<version>
docker push <registry-host>/<registry-user>/hello-world:<version>
```

Create the function on DataEngine:
```sh
vastde functions create \
 --name hello-world \
 --container-registry <registry-name-on-vms> \
 --artifact-source <registry-user>/hello-world  \
 --image-tag <version>
```

```sh
#vastde functions create output
Function created: hello-world
Name: hello-world
Tags: []
GUID: GUID
Owner: [id: 477, id-type: vid]
Created At: 2026-03-18T18:50:47Z
Updated At: 2026-03-18T18:50:47Z
VRN: vast:dataengine:functions:hello-world
Last Revision: 1
```

### 2. Set up Trigger

Create a cron trigger:
```sh
vastde triggers create \
    --name schedule-20m-trigger \
    --type Schedule \
    --description "Schedule trigger that runs every 20 minutes" \
    --tags ["every-20-minutes"] \
    --cron-schedule "0 0/20 * ? * * *"
```

```sh
#vastde triggers create output
- [ ] TODO
```

STOPPED HERE

### 3. Deploy Pipeline

Create a pipeline connecting the trigger to the function using `pipeline-config.yaml`:

```sh
vastde pipelines create \
    --config pipeline-config.yaml \
    --secret-file config.yaml
```

```sh
# vastde pipelines create output
Pipeline created: hello-vast-pipeline
```

BLOCKED HERE

Tail the logs to verify the function is being invoked:

```sh
vastde logs tail hello-vast-pipeline --function hello-world
```

```sh
#vastde pipelines create output

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
