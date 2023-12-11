import pandas as pd

data = {'A': 10, 'B': 20, 'C': 10, 'D': 30, 'E': 20}
my_series = pd.Series(data)

print("Original Series:")
print(my_series)

min_ranks_first = my_series.rank(method='first', ascending=True)

max_ranks_max = my_series.rank(method='max', ascending=True)

print("\nMinimum Ranks (using 'first' method):")
print(min_ranks_first)

print("\nMaximum Ranks (using 'max' method):")
print(max_ranks_max)
