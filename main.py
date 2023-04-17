import numpy as np #imports umpy
import matplotlib.pyplot as plt #imports graphs
import pandas as pd #imports data processing 
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#opens the data, sets it as a table using the 3rd column as the index as this is the unique piece of data
datafile = pd.read_csv('adult.csv', index_col = [2])

# drops any null data from the data set
datafile.dropna(inplace = True)

#transform data using standard scaler to plot easier
scaler = StandardScaler()
datafile.columns = datafile.columns.to_series().apply(lambda x: x.strip())
datafile[["age_t", "educationNum_t", "capitolGain_t", "capitolLoss_t", "hours_t"]] = scaler.fit_transform(datafile[["age", "educationNum", "capitolGain", "capitolLoss", "hours"]])
#print(datafile)

#function to find optimum number of clusters, k
def findKnumber(data, max_k):
    means = []
    inertias = []
    
    for k in range (1, max_k):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        
        means.append(k)
        inertias.append(kmeans.inertia_)
        
    fig =plt.subplots(figsize=(10,5))
    plt.plot(means, inertias, 'o-')
    plt.xlabel('Number of clusters')
    plt.ylabel('inertia')
    plt.grid(True)
    plt.show()
    
#call function to find k
findKnumber(datafile[["age_t", "educationNum_t", "capitolGain_t", "capitolLoss_t", "hours_t"]], 10)

#applying Kmeans algorithm
#elbow graph suggest 5 or 6 clusters 
kmeans = KMeans 
