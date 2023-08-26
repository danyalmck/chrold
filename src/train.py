import mlflow
import numpy as np
import pandas as pd


def train():
    # your code
    df = pd.read_csv("")

    # return id
    mlflow.log_param("run id", mlflow.active_run().info.run_id)
    return mlflow.active_run().info.run_id
