# Prefect Pipeline
---
This repository contains prefect code that is deployable via pipelines

**This directory contains the following resources**

- **flows** ( folder containing prefect flows )
- **tasks** ( folder containing prefect tasks )
- **utils** ( folder containing prefect config )
- **azure-pipeline.yml** ( azure devops pipeline yaml file that contains steps to deploy prefect flows )
- **job_template.yaml** ( needed by the flow in order to always pull latest image PullPolicy=Always )
- **templates** (folder containing azure pipelines templates)

Prerequisites:
- Prefect server up and running in Kubernetes
- Prefect agent of type Kubernetes with labels prefect
- Prefect project with name prefect
- Agent pool in Azure DevOps with name private-agent that has access to the prefect-server
- Storage Account Connection string where we can store our flows


**How it works**
---
The main idea behind this solution is to provide a way to develop tasks separately from Flows and be able to dynamically import them without unneccesarily registering the Flow.

We are keeping our code DRY and this is why we import pipeline templates.

Any changes to files inside flows/ tasks/ or utils/ will trigger the pipeline.

Flows and Agents of type kubernetes must have matching labels otherwise flows may not be picked up by any agent.

**Contributors**
Nikolay Vaklinov, Aksel Handzhiev and Boris Gaganelov
