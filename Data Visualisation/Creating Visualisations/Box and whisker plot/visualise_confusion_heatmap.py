import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Load model from pickle
with open('logistic_regression_demo.mdl', 'rb') as file:
    loaded_model = pickle.load(file)


# Load csv files
logistic_test_x = pd.read_csv('logistic_test_x.csv')
logistic_test_y = pd.read_csv('logistic_test_y.csv')


# Predictions
logistic_predictions = loaded_model.predict(logistic_test_x)


# Calculate confusion matrix
conf_matrix = confusion_matrix(logistic_test_y, logistic_predictions)

# Plot heatmap
plt.figure(figsize=(1024/100, 768/100), dpi=100)
sns.heatmap(conf_matrix, annot=True, fmt='d', annot_kws={"fontsize":16, "color":'white'}, cmap='seismic',
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted', fontsize=16)
plt.ylabel('Actual', fontsize=16)
plt.title('Confusion Matrix', fontsize=16)


# Save as JPEG image
plt.savefig('Logistic Visualisation Demo.jpg', format='jpg')


plt.show()















