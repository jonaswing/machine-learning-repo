import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, Normalizer


# Import the Risk data set and display its shape
data = pd.read_csv('Risk.csv')
print(data.shape)


# Replace missing string values with the most common value
data.fillna(data.select_dtypes(include='object').mode().iloc[0], inplace=True)

# Make string values numerical
mapping = {'Low': 0, 'Medium': 1, 'High': 2}
data['y'] = data['y'].map(mapping)


# Separate features (X) and target variable (y)
X = data.drop('y', axis=1)
y = data['y']

# Split the data into training and test sets (90/10 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1, random_state=1)

# Check the shapes of the resulting arrays
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Impute missing numeric values with the average value for each feature
numeric_imputer = SimpleImputer(strategy='mean')
X_train_numeric_imputed = numeric_imputer.fit_transform(X_train.select_dtypes(include='number'))
X_test_numeric_imputed = numeric_imputer.transform(X_test.select_dtypes(include='number'))

# Scale numeric values to fall within the range -1 to 1
scaler = MinMaxScaler(feature_range=(-1, 1))
X_train_scaled = scaler.fit_transform(X_train_numeric_imputed)
X_test_scaled = scaler.transform(X_test_numeric_imputed)

# Apply l1 normalization to the data
normalizer = Normalizer(norm='l1')
X_train_normalized = normalizer.fit_transform(X_train_scaled)
X_test_normalized = normalizer.transform(X_test_scaled)

# Concatenate the processed numeric features with non-numeric features
X_train_processed = pd.concat([X_train_normalized, X_train.select_dtypes(exclude='number')], axis=1)
X_test_processed = pd.concat([X_test_normalized, X_test.select_dtypes(exclude='number')], axis=1)

# Combine processed features with labels for training data
Xy_train = pd.concat([X_train_processed, y_train], axis=1)

# Combine processed features with labels for test data
Xy_test = pd.concat([X_test_processed, y_test], axis=1)

Xy_train.to_csv('Risk_train.csv', header=True, index=False)
Xy_test.to_csv('Risk_test.csv', header=True, index=False)








