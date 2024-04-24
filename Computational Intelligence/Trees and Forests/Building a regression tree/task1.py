import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer
import matplotlib.pyplot as plt


# Import dataset
data = pd.read_csv('IRIS.csv')
df = pd.DataFrame(data)


# PRE PROCESSING
# Fill
df.fillna(df.mean(), inplace=True)
# Encode species column
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

print(df.head(60))

# Specify target
X = df.drop('species', axis=1)
y = df['species']


# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)


# Train model
model = DecisionTreeClassifier(random_state=1, ccp_alpha=0.01)
model.fit(X_train, y_train)


# Use the model to predict the output values for the test data.
y_pred_train = model.predict(X_train)

# Use the model to predict the output values for the test data.
y_pred_test = model.predict(X_test)


# Perform k-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)  # 5-fold cross-validation
print("\nCross-validation scores:", cv_scores)
print("Mean CV accuracy:", np.mean(cv_scores))

# Print scores on train and test data
print("\nTraining data score: ", accuracy_score(y_train, y_pred_train))
print("Testing data score: ", accuracy_score(y_test, y_pred_test))


# Display decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, filled=True, feature_names=X.columns, class_names=label_encoder.classes_)
plt.show()






