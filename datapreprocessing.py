#section 2, part 1: Data preprocessing 

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset

dataset = pd.read_csv('Data.csv')

#creating a matrix of features 
x = dataset.iloc[:, :-1].values
print(x)

#creating depenet variable vector 
y = dataset.iloc[:, 3].values