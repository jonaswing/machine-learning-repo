import pandas as pd


movies_1 = pd.read_csv('movies_part_1.csv')
movies_1 = pd.DataFrame(movies_1)
print("Movies_1 shape: ", movies_1.shape)

movies_2 = pd.read_csv('movies_part_2.csv')
movies_2 = pd.DataFrame(movies_2)
print("Movies_2 shape: ", movies_2.shape)

movies_3 = pd.read_csv('movies_part_3.csv')
movies_3 = pd.DataFrame(movies_3)
print("Movies_3 shape: ", movies_3.shape, "\n")


# Remove Nan rows in movies_1
movies_1 = movies_1.dropna(how='all')
movies_1.to_csv('movies1.csv')


# Append movies_2 to movies_1
movies_2_and_1 = movies_1.merge(movies_2, how='outer')
print("Movies_1_and_2 shape: \n",  movies_2_and_1.shape, "\n", movies_2_and_1.head(10), "\n")


# Add columns from movies_3 to movies_2_and_1
combined = movies_3.merge(movies_2_and_1, how='outer')
print("Movies 1,2,3: \n", combined.shape, "\n", combined.head(10), "\n")
combined.to_csv('movies123.csv', index=False)

# Check for missing values in the DataFrame before filling
print(combined.isnull().sum(), "\n")

columns_to_fill = ['vote_average', 'vote_count', 'revenue', 'runtime', 'popularity']
for column in columns_to_fill:
    median_value = combined[column].median()
    combined[column].fillna(median_value, inplace=True)

# Check for missing values in the DataFrame after filling
print(combined.isnull().sum(), "\n")

combined.to_csv('filled.csv', index=False)

strings_to_fill = ['release_date', 'original_language', 'original_title']
for string in strings_to_fill:
    most_frequent = combined[string].mode()[0]
    combined[string].fillna(most_frequent, inplace=True)

# Convert 'release_date' to datetime
combined['release_date'] = pd.to_datetime(combined['release_date'])

print(combined.isnull().sum(), "\n")

# Sort by release_date and popularity
combined = combined.sort_values(by=['release_date', 'popularity'], ascending=False)
combined.to_csv('sorted.csv', index=False)


# Calculate the mean revenue for each vote_average
mean_revenue_by_vote_average = combined.groupby('vote_average')['revenue'].mean()

print(mean_revenue_by_vote_average)