# -*- coding: utf-8 -*-
"""polynomial_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hntNLZKAtB7oH5_xPSj_3xGgfpqN3uHy

# Polynomial Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

"""## Training the Linear Regression model on the whole dataset"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,y)

"""## Training the Polynomial Regression model on the whole dataset"""

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
reg = LinearRegression()
reg.fit(X_poly,y)

"""## Visualising the Linear Regression results"""

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Polynomial Regression results"""

plt.scatter(X, y, color = 'red')
plt.plot(X, reg.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Polynomial Regression results (for higher resolution and smoother curve)"""

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid,reg.predict(poly_reg.fit_transform(X_grid)) , color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Predicting a new result with Linear Regression"""

regressor.predict([[7.6]])

"""## Predicting a new result with Polynomial Regression"""

reg.predict(poly_reg.fit_transform([[7.6]]))

