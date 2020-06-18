import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()
#print(prod_per_year)
X = prod_per_year['year']
X = X.values.reshape(-1, 1)
#print(X)
y = prod_per_year['totalprod']

plt.scatter(X, y)
plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)
y_predict = regr.predict(X)
print(regr.coef_[0])
print(regr.intercept_)

plt.plot(X, y_predict)
plt.show()

X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)
#You can think of reshape() as rotating this array. Rather than one big row of numbers, X_future is now a big column of numbers — there’s one number in each row.

future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()

