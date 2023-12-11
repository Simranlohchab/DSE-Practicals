import numpy as np

m, n = 5, 4 
original_array = np.random.randint(10, 100, size=(m, n))

print("Original Array:")
print(original_array)

row_to_swap1 = 0
row_to_swap2 = 1
array_after_row_swap = original_array.copy()
array_after_row_swap[row_to_swap1], array_after_row_swap[row_to_swap2] = (
    array_after_row_swap[row_to_swap2],
    array_after_row_swap[row_to_swap1],
)

column_to_reverse = 1
array_after_column_reverse = original_array.copy()
array_after_column_reverse[:, column_to_reverse] = np.flip(
    array_after_column_reverse[:, column_to_reverse]
)

print("\nArray after swapping rows:")
print(array_after_row_swap)

print("\nArray after reversing a specified column:")
print(array_after_column_reverse)
