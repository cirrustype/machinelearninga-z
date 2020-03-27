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

#Encoding cat variables into numbers
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

#turning country into three dummy variables
#0=no, 1=yes
#france, spain, germany. it goes in order of the first observations
ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x), dtype=np.float)

#encoding the y data 
#0=no, 1=yes
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)





