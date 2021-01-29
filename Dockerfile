FROM prefecthq/prefect

ARG STORAGE_CONNECTION_STRING=PRIVDED_BY_THE_PIPELINE

ARG IMAGE=PROVIDED_BY_THE_PIPELINE

ENV IMAGE_URL=$IMAGE

ENV AZURE_STORAGE_CONNECTION_STRING=$STORAGE_CONNECTION_STRING

RUN mkdir -p /prefect/tasks/ /prefect/utils/

COPY utils/ /prefect/utils/

COPY tasks/ /prefect/tasks/

ENV PYTHONPATH="${PYTHONPATH}:/prefect/tasks/:/prefect/utils/"

COPY job_template.yaml /prefect/

WORKDIR prefect
