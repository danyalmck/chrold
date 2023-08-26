import mlflow
import numpy as np
import pandas as pd

def train():
    df = pd.read_csv("")
    k_means = KMeans(n_clusters=5).fit(df)
    print(k_means.clusters)
    return mlflow.active_run().info.run_id



class KMeans:
    
    def __init__(self, n_clusters=4):
        self.K = n_clusters
        
    def fit(self, X):
        self.setup(X)
        while not np.all(self.clusters == self.prev_clusters) :
            self.prev_clusters = self.clusters
            self.clusters = self.predict(X)
            self.update_centroid(X)
        return self
        
    def predict(self, X):
        return np.apply_along_axis(self.calc_cluster, 1, X)

    def setup(self, X):
        # This first random assignment can be problematic
        # As makes bias for cluster formation
        self.centroids = X.iloc[np.random.choice(len(X), self.K, replace=False)]
        self.intial_centroids = self.centroids
        self.prev_clusters,  self.clusters = None, np.zeros(len(X))

    def calc_cluster(self, x):
        return np.argmin(np.sqrt(np.sum((self.centroids - x)**2, axis=1)))

    def update_centroid(self, X):
        self.centroids = np.array([np.mean(X[self.clusters == k], axis=0)  for k in range(self.K)])