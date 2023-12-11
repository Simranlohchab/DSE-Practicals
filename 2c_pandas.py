import pandas as pd

data = {'A': 10, 'B': 20, 'C': 5, 'D': 30, 'E': 15}
my_series = pd.Series(data)

print("Original Series:")
print(my_series)

min_index = my_series.idxmin()

max_index = my_series.idxmax()

print("\nIndex of the Minimum Element:", min_index)
print("Index of the Maximum Element:", max_index)
