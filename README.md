# Chrold

Run your ML commit directly on production

## In a Nutshell

Chrold is a free and easy-to-use repository template for your Machine Learning project which lets you run your commit directly on production with zero effort.

It's an MLOps pipeline which build, train, track your models and finally, you can deploy your desired version as a Docker container on production.

## Quick Start

* Create an account in [Databricks](https://databricks.com/try-databricks) (the community edition is free)
    - If you want to self-host the tracking server, see the Advanced Usage section.
* Set up these variables as your [repository secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):
    - ```DATABRICKS_HOST=<YOUR_HOST> (for example: https://community.cloud.databricks.com)```
    - ```DATABRICKS_USERNAME=<YOUR_USERNAME>```
    - ```DATABRICKS_PASSWORD=<YOUR_PASSWORD>```
    - ```MLFLOW_TRACKING_URI=<DATABRICKS_HOST>```
    - ```MLFLOW_TRACKING_USERNAME=<DATABRICKS_USERNAME>```
    - ```MLFLOW_TRACKING_PASSWORD=<DATABRICKS_PASSWORD>```
* Implement the ```train``` function in ```src/train.py``` and done!
