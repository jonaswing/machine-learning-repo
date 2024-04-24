import pandas as pd

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers',
                      sep='|',
                      header=None,
                      names=user_cols,
                      skiprows=[2])

# Choose the first ten rows of the occupation column
first_ten = users['occupation']
print(first_ten[0:10])
print()

# Choose the first ten rows of the occupation column using .head(10)
print(users['occupation'].head(10))
print()

# This is faster
print(users.occupation[0:11])

# print(users[0:10])
