import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# Check Number of Dimensions

print(arr.ndim)

# Checking the Data Type of an Array
print(arr.dtype)

# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# Reshape From 1-D to 2-D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# search
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# sort
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))