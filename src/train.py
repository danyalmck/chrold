import pandas as pd
from examples import logistic_regression


# Your code
def train(current_run, warm_start, warm_start_run_id):
    df = pd.read_csv("https://kwargs.s3.ir-thr-at1.arvanstorage.ir/Car_prices_classification.csv")
    score = logistic_regression.train(current_run, warm_start, warm_start_run_id, df)
    print(score)

    return
