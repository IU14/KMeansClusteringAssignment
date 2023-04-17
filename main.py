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
datafile[["age_t", "educationNum_t"]] = scaler.fit_transform(datafile[["age", "educationNum"]])
#print(datafile)

#function to find optimum number of clusters, produces an elbow graph
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
findKnumber(datafile[["age_t", "educationNum_t"]], 10)

#applying Kmeans algorithm
#elbow graph suggests 5 clusters  
kmeans = KMeans(n_clusters=5)
kmeans.fit(datafile[["age_t", "educationNum_t"]])
datafile['kmeans_5'] = kmeans.labels_
#print(datafile)

#plot the results using age and eductaion num as the axis. 
#plt.scatter(x=datafile['age'], y=datafile['educationNum'], c=datafile['kmeans_5'])
#plt.xlim(15, 100)
#plt.ylim(0, 20)
#plt.show()

#plot results with varrying clusters
for k in range(1, 6):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(datafile[["age_t", "educationNum_t"]])
    datafile[f'KMeans_{k}'] = kmeans.labels_
    #print(datafile)
    fig, axs = plt.subplots(nrows =1, ncols =5, figsize =(20,5))
    for i, ax in enumerate(fig.axes):
        ax.scatter(x=datafile['age'], y=datafile['educationNum'], c=datafile[f'KMeans_{i}'])
        ax.set_xlim(15, 100)
        ax.set_ylim(0, 20)
        ax.set_title(f'N Clusters: {i}') 