import mlflow
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Your code
def train(warm_start, run_id):
    df = pd.read_csv("https://kwargs.s3.ir-thr-at1.arvanstorage.ir/Car_prices_classification.csv")

    if warm_start:
        model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")
    else:
        model = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=100)

    # Only the column 'generation_name' has NaN values.
    # To handle this issue, we replaced the NaN for each record with the concatenation of its model and mark!
    processed_df = df.copy()
    processed_df['generation_name'] = np.where(processed_df['generation_name'].isnull(), processed_df['mark'] + processed_df['model'], processed_df['generation_name'])

    # We drop the column 'city' as it has almost no effect on the results and just increases our dimensionality
    new_df = processed_df.drop('city', axis=1)
    # Binning the year, mileage and vol_engine features
    new_df['mileage'] = pd.qcut(new_df['mileage'], 50, labels=[i for i in range(50)])
    new_df['year'] = pd.qcut(new_df['year'], 5, labels=[i for i in range(5)])
    new_df['vol_engine'] = pd.qcut(new_df['vol_engine'], 15, labels=[i for i in range(15)])
    # Encoding the categorical features using sklearn OneHotEncoder
    transformer = make_column_transformer(
        (OneHotEncoder(), ['mark', 'model', 'generation_name', 'year', 'mileage', 'fuel', 'vol_engine', 'province']),
        remainder='passthrough')
    transformed = transformer.fit_transform(new_df)
    transformed_df = pd.DataFrame.sparse.from_spmatrix(transformed, columns=transformer.get_feature_names_out())

    # We have enough data, so we don't need cross-validation. We simply split data with 70/30
    # The reason is empirical as we tested 80/20, 70/30 and 60/40 and the maximum score of these were 70/30
    y = transformed_df.remainder__price_class
    X = transformed_df.drop('remainder__price_class', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model.fit(X_train, y_train)
    print(model.score(X_test, y_test))

    # return id
    mlflow.log_param("run id", mlflow.active_run().info.run_id)
    return mlflow.active_run().info.run_id
