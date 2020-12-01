import numpy as np
import pandas as pd
from sklearn import cluster
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn import cluster
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# data = pd.read_csv("trend_ca_20201026.csv")
#
# x= data.values[:,4:9]
# print(x)
# y = data.values[:,3]
# print(y)
# scaled_data = scale(x)
# n_samples, n_features = scaled_data.shape
# n_digits = len(np.unique(y))
# Y2 = LabelEncoder().fit_transform(y)
# aff = ["euclidean", "l1", "l2", "manhattan", "cosine"]
# link = ["ward", "complete", "average"]
# for a in aff:
#     for l in link:
#         if(l=="ward" and a!="euclidean"):
#             continue
#         else:
#             print(a,l)
#             model = cluster.AgglomerativeClustering(n_clusters=n_digits, linkage=l, affinity=a)
#             model.fit(scaled_data)
#             # run these scores on juptr in order to work
#             # print(metrics.silhouette_score(scaled_data, model.labels_))
#             print(metrics.completeness_score(Y2, model.labels_))
#             print(metrics.homogeneity_score(Y2, model.labels_))

data = pd.read_csv("scores.csv")
score = ["Silhouette ","Completeness ", "Homogeneity "]
data1 = data.groupby("Type")[score].sum()

data1.plot.bar()
plt.ylabel("Scores")
plt.show()
#
data = pd.read_csv("trend_ca_20201026.csv")

x= data.values[:,4:9]
print(x)
y = data.values[:,3]
print(y)
scaled_data = scale(x)
n_samples, n_features = scaled_data.shape
n_digits = len(np.unique(y))
Y2 = LabelEncoder().fit_transform(y)
aff = ["euclidean", "l1", "l2", "manhattan", "cosine"]
link = ["ward", "complete", "average"]
for a in aff:
    for l in link:
        if(l=="ward" and a!="euclidean"):
            continue
        else:
            print(a,l)
            model = cluster.AgglomerativeClustering(n_clusters=n_digits, linkage=l, affinity=a)
            model.fit(scaled_data)
            # run these scores on juptr in order to work
            print(metrics.silhouette_score(scaled_data, model.labels_))
            print(metrics.completeness_score(Y2, model.labels_))
            print(metrics.homogeneity_score(Y2, model.labels_))

silhouette_coefficients = []
completeness_coefficients = []
homogeneity_coefficients = []
for k in range(2, 50):
    kmeans = cluster.KMeans(n_clusters=k)
    kmeans.fit(scaled_data)
    score = metrics.silhouette_score(scaled_data, kmeans.labels_)
    silhouette_coefficients.append(score)
    lol = metrics.completeness_score(Y2, kmeans.labels_)
    completeness_coefficients.append(lol)
    ff= metrics.homogeneity_score(Y2, kmeans.labels_)
    homogeneity_coefficients.append(ff)
plt.plot(range(2,50),silhouette_coefficients, label= "Silhouette")
plt.plot(range(2,50),completeness_coefficients, label= "Completeness")
plt.plot(range(2,50),homogeneity_coefficients, label= "Homogeneity")
plt.xticks([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48])
plt.title("Results of Varying Clusters - KMeans")
plt.xlabel("Number of Clusters")
plt.ylabel("Scores")
plt.legend()
plt.show()
