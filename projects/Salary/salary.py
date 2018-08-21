import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline


salary = pd.read_csv('salary.csv')

X = salary['YearsExperience'].values
Y = salary['Salary'].values

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)


# This is Common Denominator
denominator = X_test.dot(X_test) - X_test.mean() * X_test.sum()

## Find m and b in y = mx + b
## Find formula for m and b in predictive_models/linear_regression

m = (X_test.dot(Y_test) - Y_test.mean() * X_test.sum()) / denominator
b = (Y_test.mean() * X_test.dot(X_test) - X_test.mean() * X_test.dot(Y_test)) / denominator

Y_pred = (m * X_test) + b

plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_pred,'r')
