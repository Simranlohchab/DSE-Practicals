import pandas as pd

# Create a Series with 5 elements
data = {'B': 10, 'A': 5, 'D': 20, 'C': 15, 'E': 25}
my_series = pd.Series(data)

# Display the original series
print("Original Series:")
print(my_series)

# Sort the series by index
sorted_by_index = my_series.sort_index()

# Sort the series by values
sorted_by_values = my_series.sort_values()

# Display the sorted series
print("\nSorted Series by Index:")
print(sorted_by_index)

print("\nSorted Series by Values:")
print(sorted_by_values)
