import mlflow
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN


def train():
    # your code
    df = pd.read_csv("https://kwargs.s3.ir-thr-at1.arvanstorage.ir/1.csv")

    coords = df.values
    dbscan = DBSCAN(eps=50, min_samples=100)
    labels = dbscan.fit_predict(coords)
    print(labels)

    # return id
    mlflow.log_param("run id", mlflow.active_run().info.run_id)
    return mlflow.active_run().info.run_id
