import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv('tic-tac-toe.data')

# Make column names
data.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Class']

# Choose target to predict
X = data.drop('Class', axis=1)
y = data['Class']

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X)

# Train and test splits
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=1)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# PREDICTIONS
predictions_classification = model.predict(X_test)

# EVALUATION
accuracy_classification = accuracy_score(y_test, predictions_classification)
print("Accuracy classification potability:", accuracy_classification)
