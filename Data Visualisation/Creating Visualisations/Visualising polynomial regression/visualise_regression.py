import pickle
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# Models
with open('linear_regression_demo.mdl', 'rb') as f:
    linear_model1 = pickle.load(f)

with open('polynomial_regression_demo.mdl', 'rb') as f:
    polynomial_model2 = pickle.load(f)


# Data
linear_and_polynomial_test_y = pd.read_csv('linear_and_polynomial_test_y.csv')
linear_test_x = pd.read_csv('linear_test_x.csv')
polynomial_test_x = pd.read_csv('polynomial_test_x.csv')


# Perform predictions using linear model
linear_predictions = linear_model1.predict(linear_test_x)

# Perform predictions using polynomial model
polynomial_predictions = polynomial_model2.predict(polynomial_test_x)



