import pandas as pd

data = pd.read_csv("bodyfatprediction.csv")

df = pd.DataFrame(data)

# Define age bins and labels
age_bins = [0, 18, 30, 50, float('inf')]
age_labels = ['Under 18', '18-30', '30-50', '50+']

# Create the 'Muscle Density' feature
df['Muscle Density'] = (df['Density'] / df['Weight']).round(4)

# Create the 'Chest to waist ratio' feature
df['Chest to abdomen ratio'] = (df['Chest'] / df['Abdomen']).round(4)

# Create the 'Age Group' feature
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

# Display the DataFrame with the new 'Age Group' feature
print(df)

# Save the updated DataFrame to a new CSV file
df.to_csv("bodyfatprediction_with_age_group.csv", index=False)
