import numpy as np

# Get user input for dimensions m and n
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Create a 2-dimensional array with random integer elements
original_array = np.random.randint(0, 10, size=(m, n))

# Print original array, shape, type, and data type
print("\nOriginal Array:")
print(original_array)

print("\nShape of the Array:", original_array.shape)
print("Type of the Array:", type(original_array))
print("Data Type of the Array:", original_array.dtype)

# Reshape the array to an n x m array
reshaped_array = original_array.reshape((n, m))

# Print the reshaped array
print("\nReshaped Array (n x m):")
print(reshaped_array)
