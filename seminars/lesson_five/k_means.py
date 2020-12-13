from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create a random 2-dimensional dataset
Data = {
    'x': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45, 38,
          43, 51, 46],
    'y': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29, 27,
          8, 7]
    }

# Create a pandas data frame for storing the 2-dimensional datset
df = DataFrame(Data, columns=['x', 'y'])

# Run kmeans with 4 different clussters
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
# Visualize results
plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float))
plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
plt.show()
