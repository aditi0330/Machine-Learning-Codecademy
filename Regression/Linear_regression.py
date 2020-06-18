import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 10
#intercept:
b = 45
y = [m*month + b for month in months]
plt.plot(months, y)
plt.plot(months, revenue, "o")

plt.show()

#Loss
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [m1*x1 + b1 for x1 in x]

#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2*x1 + b2 for x1 in x]

total_loss1 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2

total_loss2 = 0
for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i]) ** 2

print(total_loss1)
print(total_loss2)

better_fit = 2

#Minimizing Loss

#Gradient Descent for Intercept
def get_gradient_at_b(x, y, m , b):
  diff = 0
  N = len(x)
  for i in range(0, len(x)):
    y_val = y[i]
    x_val = x[i]
    diff += (y_val - ((m * x_val) + b))
  
  b_gradient = -(2/N) * diff
  return b_gradient

def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val * (y_val - ((m * x_val) + b))

    m_gradient = -(2/N)*diff
    return m_gradient

# Define your step_gradient function here
def step_gradient(x, y, b_current, m_current):
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * m_gradient)
  return (b, m)

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b, m = step_gradient(months, revenue, b, m)
print(b, m)

from gradient_descent_funcs import gradient_descent
import pandas as pd

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]
b, m = gradient_descent(X, y, 0.0001, 1000)
y_predictions = [element*m + b for element in X]

plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X, y_predictions, 'o')
plt.show()

#Scikit Learn
import codecademylib3_seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)
sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales_predict)
plt.plot(temperature, sales, 'o')
plt.show()

#Boston Housing
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Boston housing dataset
boston = load_boston()

df = pd.DataFrame(boston.data, columns = boston.feature_names)

# Set the x-values to the nitrogen oxide concentration:
X = df[['NOX']]
# Y-values are the prices:
y = boston.target

# Can we do linear regression on this?
line_fitter = LinearRegression()
line_fitter.fit(X, y)
y_predict = line_fitter.predict(X)



plt.scatter(X, y, alpha=0.4)
# Plot line here:
plt.plot(X, y_predict)
plt.title("Boston Housing Dataset")
plt.xlabel("Nitric Oxides Concentration")
plt.ylabel("House Price ($)")
plt.show()