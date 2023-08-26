import mlflow
from src.train import train

user_name = "dm.enrollment@protonmail.com"
experiment_name = "chrold-exp1"
tracking_ui = "databricks"
mlflow.set_tracking_uri(tracking_ui)
mlflow.set_experiment(f"/Users/{user_name}/{experiment_name}")
mlflow.autolog()

if __name__ == "__main__":
    run_id = train()
    mlflow.log_param("run id", run_id)
    with open("r_id.txt", "w") as file:
        file.write(run_id)