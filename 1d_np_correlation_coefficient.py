import numpy as np

# Create random arrays of the same size
size = 100  # Change the size according to your requirements

Array1 = np.random.rand(size)
Array2 = np.random.rand(size)
Array3 = np.random.rand(size)

# Subtract Array2 from Array3 and store in Array4
Array4 = Array3 - Array2

# Create Array5 with two times the values in Array1
Array5 = 2 * Array1

# Calculate covariance between Array1 and Array4
covariance_array1_array4 = np.cov(Array1, Array4)[0, 1]

# Calculate covariance between Array1 and Array5
covariance_array1_array5 = np.cov(Array1, Array5)[0, 1]

# Calculate correlation between Array1 and Array4
correlation_array1_array4 = np.corrcoef(Array1, Array4)[0, 1]

# Calculate correlation between Array1 and Array5
correlation_array1_array5 = np.corrcoef(Array1, Array5)[0, 1]

# Print the results
print("Array1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)

print("\nCovariance between Array1 and Array4:", covariance_array1_array4)
print("Covariance between Array1 and Array5:", covariance_array1_array5)
print("Correlation between Array1 and Array4:", correlation_array1_array4)
print("Correlation between Array1 and Array5:", correlation_array1_array5)
