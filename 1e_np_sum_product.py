import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Create random arrays of size 10
size = 10

Array1 = np.random.rand(size)
Array2 = np.random.rand(size)

# Find the sum of the first half of both arrays
sum_first_half = np.sum(Array1[:size//2]) + np.sum(Array2[:size//2])

# Find the product of the second half of both arrays
product_second_half = np.product(Array1[size//2:]) * np.product(Array2[size//2:])

# Print the results
print("Array1:", Array1)
print("Array2:", Array2)

print("\nSum of the first half of both arrays:", sum_first_half)
print("Product of the second half of both arrays:", product_second_half)
