#section 2, part 1: Data preprocessing 

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk

#importing the dataset

dataset = pd.read_csv('Data.csv')

#creating a matrix of features 
x = dataset.iloc[:, :-1].values


#creating depenet variable vector 
y = dataset.iloc[:, 3].values


#imputing missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])



