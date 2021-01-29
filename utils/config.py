from prefect.storage import Azure
from prefect.run_configs import KubernetesRun
import os

azure_store = Azure(container="prefect")

kubernetes_run = KubernetesRun(
    image=os.environ.get("IMAGE_URL"),
    job_template_path=os.environ.get("JOB_TEMPLATE_PATH", "./job_template.yaml"),
    labels=["prefect"],
)
