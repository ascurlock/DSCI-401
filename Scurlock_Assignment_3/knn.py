# For Assignment 3 - This is what will go into your "Knn.py" file
# For Assignment 3 - This is what will go into your "Knn.py" file
import pandas as pd
import numpy as np
from statistics import mode
from scipy.spatial.distance import euclidean

class KNN:
    def __init__(self, k, distance_f):
        #TODO: create instance variables that store these values
        self.k = k
        self.distance_f = distance_f
        self.x = None
        self.y = None
        
    def fit(self, x, y):
        #Notes: 1) You will need to check types and convert convert to numpy arrays if the x and y are dataframes
        if isinstance(x, pd.DataFrame):
           # print('x is a dataframe')
            self.x = x.values
          #  print(self.x)
        else:
            self.x = x
        if isinstance(y, pd.DataFrame):
            self.y = y.values
        else:
            self.y = y
       # print(self.y)
       # return x
            
    def predict(self, x):
         #TODO: Inplement prediction logic and return list/array of predicted lables
        if isinstance(x, pd.DataFrame):
            x = x.values
        xtrain = list(zip(self.x, self.y))
        predictions = np.array([])
        for i in range(len(x)): # Predicting data
            distances = [100] * self.k # This gets the list of distances
            result = [2] * self.k # The y value that corresponds to each of the closest variables
            for j in range(len(xtrain)): #Saved data
                if euclidean(x[i,:], xtrain[j][0]) < max(distances):
                    max_index = distances.index(max(distances))
                    distances[max_index] = euclidean(x[i,:], xtrain[j][0])
                    result[max_index] = xtrain[j][1]
            predictions = np.append (predictions, mode(result))
        return predictions