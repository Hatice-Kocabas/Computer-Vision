import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def compute_euclidean(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))


def cluster_data(data, K, max_iterations=100):

    centroid_points = data[np.random.choice(data.shape[0], K, replace=False)]
    
    for _ in range(max_iterations):
        cluster_labels = []
        for sample in data:
            distances = [compute_euclidean(sample, centroid) for centroid in centroid_points]
            cluster_label= np.argmin(distances)
            cluster_labels.append(cluster_label)

        cluster_labels = np.array(cluster_labels)
        
        new_centroid_points = []
        for i in range(K):
            cluster_points = data[cluster_labels == i]
            new_centroid_point = np.mean(cluster_points, axis=0)
            new_centroid_points.append(new_centroid_point)
        
        new_centroid_points = np.array(new_centroid_points)
        
        if np.all(centroid_points == new_centroid_points):
            break
        
        centroid_points = new_centroid_points
    
    return centroid_points, cluster_labels




iris = load_iris()
data = iris.data

K = 8 
centroid_points, cluster_labels = cluster_data(data, K)


plt.figure(figsize=(8, 6))

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange'] 
for i in range(K):
    cluster_points = data[cluster_labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i}')

plt.scatter(centroid_points[:, 0], centroid_points[:, 1], marker='+', s=100, c='black', label='Centroid points')
plt.title('K-means Clustering Output')
plt.xlabel('Attribute 1')
plt.ylabel('Attribute 2')
plt.legend()
plt.show()
