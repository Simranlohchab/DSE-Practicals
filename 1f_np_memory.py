import numpy as np

random_array = np.random.rand(100, 100)

memory_size = random_array.nbytes

print("Array shape:", random_array.shape)
print("Memory size occupied by the array (in bytes):", memory_size)

