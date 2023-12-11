import numpy as np

arr1 = np.random.rand(3, 4)

print("Original Array:")
print(arr1)

mean_values = np.mean(arr1, axis=1)

variance_values = np.var(arr1, axis=1)

std_dev_values = np.std(arr1, axis=1)

print("\nMean along the second axis:")
print(mean_values)

print("\nVariance along the second axis:")
print(variance_values)

print("\nStandard Deviation along the second axis:")
print(std_dev_values)
