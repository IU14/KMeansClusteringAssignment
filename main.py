import numpy as np #imports algebra 
import matplotlib 
import matplotlib.pyplot as plt #imports graphs
import pandas as pd #imports data processing 
#from sklearn.cluster import KMeans

#open files & extract the data 
file1 = open("/workspace/KMeansClusteringAssignment/DataSets/adult.data", "r")

for line in file1
    datalines = file1.readline()
    list1 = datalines.split(',')
    features.append([float(list1[0].strip()),float(list1[1].strip())]) #
file1.close()

file2 = open("/workspace/KMeansClusteringAssignment/DataSets/adult.test", "r")

for line in file2
    datalines2 =  file2.readline()
    list2 = datalines2.split (',')
    featuers.append([float(list2[0].strip()),float(list2[1].strip())]) #
file2.close()

#add both extracted data lists together
allData = list1 + list2
print(allData)


#set number of clusters
k =


