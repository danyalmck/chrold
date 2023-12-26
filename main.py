import mlflow
import os
from src.train import train


UESRNAME = os.environ.get("DATABRICKS_USERNAME")
EXPERIMENT = "perceptron-exp-1"
TRACKING_UI = "databricks"

mlflow.set_tracking_uri(TRACKING_UI)
mlflow.set_experiment(f"/Users/{UESRNAME}/{EXPERIMENT}")
mlflow.autolog()

if __name__ == "__main__":
    with mlflow.start_run() as run:
        mlflow.log_param("run id", run.info.run_id)
        train(run, False, "")
        with open("r_id.txt", "w") as file:
            file.write(run.info.run_id)