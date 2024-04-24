# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, normalize

# Step 2: Import the data set into a Pandas DataFrame
url = "data0303.csv"  # Replace with the actual path to the downloaded CSV file
df = pd.read_csv(url)

# Step 3: Display the current shape and the first 20 rows of the DataFrame
print("Current shape of the DataFrame:", df.shape)
print("First 20 rows of the DataFrame:\n", df.head(20))

# Step 4: Perform an 80/20 split of the data set
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Extract features (X) and class labels (y) for training and test sets
train_x = train_df.drop(columns=['class'])
train_y = train_df['class']
test_x = test_df.drop(columns=['class'])
test_y = test_df['class']

# Step 5a: Test the StandardScaler, MinMaxScaler, and MaxAbsScaler on the training set
scalers = [StandardScaler(), MinMaxScaler(), MaxAbsScaler()]

for scaler in scalers:
    scaled_train_x = scaler.fit_transform(train_x)
    print(f"Results after applying {type(scaler).__name__}:\n", scaled_train_x)

    # You may visualize or analyze the results here

# Choose one scaler and permanently apply the results
chosen_scaler = StandardScaler()  # Change this based on your analysis
train_x_scaled = chosen_scaler.fit_transform(train_x)

# Step 5b: Test l1, l2, and max normalization on the revised data set
normalizations = ['l1', 'l2', 'max']

for norm in normalizations:
    normalized_train_x = normalize(train_x_scaled, norm=norm, axis=0)
    print(f"Results after applying {norm} normalization:\n", normalized_train_x)

    # You may visualize or analyze the results here

# Choose one normalization method and permanently apply the results
chosen_norm = 'l1'  # Change this based on your analysis
train_x_normalized = normalize(train_x_scaled, norm=chosen_norm, axis=0)

# Step 6: Combine the updated features of the training set with its class labels
train_updated_df = pd.concat([pd.DataFrame(train_x_normalized, columns=train_x.columns), train_y], axis=1)

# Step 7: Save the DataFrame to file as 0303_updated.csv
train_updated_df.to_csv("0303_updated.csv", index=False)