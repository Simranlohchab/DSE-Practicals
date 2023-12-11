import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Create a DataFrame with at least 3 columns and 50 rows
data = {'Column1': np.random.rand(50), 'Column2': np.random.rand(50), 'Column3': np.random.rand(50)}

# Replace 10% of values with null
indices_to_replace = np.random.choice(range(50), size=int(0.1 * 50), replace=False)
for col in data.keys():
    data[col][indices_to_replace] = np.nan

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# a. Identify and count missing values in a DataFrame
missing_values_count = df.isnull().sum()
print("\nMissing Values Count:")
print(missing_values_count)

# b. Drop the column having more than 5 null values
df = df.dropna(thresh=len(df) - 5, axis=1)

# c. Identify the row label having the maximum sum of all values in a row and drop that row
max_sum_row_label = df.sum(axis=1).idxmax()
df = df.drop(index=max_sum_row_label)

# d. Sort the DataFrame based on the first column
df = df.sort_values(by='Column1')

# e. Remove all duplicates from the first column
df = df.drop_duplicates(subset='Column1')

# f. Find the correlation between the first and second column and covariance between the second and third column
correlation_column1_column2 = df['Column1'].corr(df['Column2'])
covariance_column2_column3 = df['Column2'].cov(df['Column3'])

# Display the results
print("\nDataFrame after Operations:")
print(df)

print("\nCorrelation between Column1 and Column2:", correlation_column1_column2)
print("Covariance between Column2 and Column3:", covariance_column2_column3)

# g. Discretize the second column and create 5 bins
df['Column2_bins'] = pd.cut(np.array(df['Column2']), bins=5)

# Display the DataFrame with the new discretized column
print("\nDataFrame with Discretized Column:")
print(df)
