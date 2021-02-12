# Azure pipelines templates
---
This folder contains azure pipeline yaml code

**This folder contains the following resources**

- **register-flows.yml** ( It registers only flows that changed )
- **docker-login.yml** ( It logs in ACR )
- **docker-build.yml** ( It builds a docker image with the help of the Dockerfile in the root directory of the project )
- **docker-push.yml** ( It pushes images that were built with docker-build.yml )


We follow the DRY method of Azure Pipelines where we split every functionaity in templates which we can reuse elsewhere.

**Contributors**
Nikolay Vaklinov
and Aksel Handzhiev
