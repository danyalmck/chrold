import mlflow
from src.train import train


UESRNAME = "dm.enrollment@protonmail.com"
EXPERIMENT = "chrold-exp1"
TRACKING_UI = "databricks"

mlflow.set_tracking_uri(TRACKING_UI)
mlflow.set_experiment(f"/Users/{UESRNAME}/{EXPERIMENT}")
mlflow.autolog()

if __name__ == "__main__":
    with mlflow.start_run() as run:
        run_id = train()
        with open("r_id.txt", "w") as file:
            file.write(run_id)