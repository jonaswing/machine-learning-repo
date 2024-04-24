# pandas under the alias pd
import pandas as pd
# import MaxAbsScaler from the scikit-learn.preprocessing module
from sklearn.preprocessing import MaxAbsScaler

# Create 3 columns of data each with 4 values.
data = [[9,2,7],
        [1,5,6],
        [1,5,1],
        [7,8,9]]


# Create a new DataFrame from the data assign names to the columns
demo = pd.DataFrame(data,columns=["Feature 1", "Feature 2", "Feature 3"])
# Display the contents of the DataFrame
print("Data set before scaling:\n", demo)

# Declare a MaxAbsScaler
scaler = MaxAbsScaler()
# Use the scaler to scale the values of each column - the data should
demo["Feature 1"] = scaler.fit_transform(demo["Feature 1"].values.reshape(-1, 1))
demo["Feature 2"] = scaler.fit_transform(demo["Feature 2"].values.reshape(-1, 1))
demo["Feature 3"] = scaler.fit_transform(demo["Feature 3"].values.reshape(-1, 1))

# Display the contents of the DataFrame
print("\nData set after scaling:\n", demo)

