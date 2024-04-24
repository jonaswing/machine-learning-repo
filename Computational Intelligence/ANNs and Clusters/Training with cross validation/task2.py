import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Load data
data = pd.read_csv('tic-tac-toe.data')

# Make column names
data.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Class']

# Choose target to predict
X = data.drop('Class', axis=1)
y = data['Class']

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X)

# Convert labels to binary
y_binary = (y == 'positive').astype(int)

# Train and test splits
split = int(0.8 * len(X_encoded))
X_train, X_test = X_encoded.iloc[:split], X_encoded.iloc[split:]
y_train, y_test = y_binary.iloc[:split], y_binary.iloc[split:]

# Build the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Sigmoid activation for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

# Evaluate the model
accuracy = model.evaluate(X_test, y_test, verbose=0)[1]
print("Accuracy classification potability:", accuracy)
