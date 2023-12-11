import numpy as np

# Create a 1D array with some zeros, non-zeros, and NaN values
original_array = np.array([1, 0, 5, 0, np.nan, 8, 0])

# Test whether elements are zero
zero_indices = np.where(original_array == 0)[0]

# Test whether elements are non-zero
non_zero_indices = np.nonzero(original_array)[0]

# Test whether elements are NaN
nan_indices = np.where(np.isnan(original_array))[0]

# Print the results
print("Original Array:", original_array)
print("\nIndices of Zero Elements:", zero_indices)
print("Indices of Non-Zero Elements:", non_zero_indices)
print("Indices of NaN Elements:", nan_indices)
