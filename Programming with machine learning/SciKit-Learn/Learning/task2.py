import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, KBinsDiscretizer


# Load the data
df = pd.read_csv('CitySales.csv')

# One-hot encoding for the CITY column
city_encoder = OneHotEncoder(sparse=False, drop='first')  # drop the first column to avoid multicollinearity
city_encoded = pd.DataFrame(city_encoder.fit_transform(df[['CITY']]), columns=df['CITY'].unique()[1:])

# Ordinal encoding for the MONTH column
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_encoder = OrdinalEncoder(categories=[month_order], dtype=int)
month_encoded = pd.DataFrame(month_encoder.fit_transform(df[['MONTH']]), columns=['Month'])

# Binning for the SALES_AMOUNT column
sales_binner = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
df['SALES_BIN'] = sales_binner.fit_transform(df[['SALES_AMOUNT']])

# Combine the results
final_df = pd.concat([city_encoded, month_encoded, df[['SALES_BIN', 'SALES_AMOUNT']]], axis=1)

# Save to file
final_df.to_csv('UpdatedCitySales.csv', index=False)
