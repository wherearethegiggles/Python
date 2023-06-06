

"""(1) Demonstrate the following Numpy functions:
  (a) Arithmetic functions:
    add(), subtract(), multiply(), divide(), floor_divide()
"""

import numpy as np

# Creating two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Using add()
result_add = np.add(arr1, arr2)
print("Addition:", result_add)

# Using subtract()
result_subtract = np.subtract(arr1, arr2)
print("Subtraction:", result_subtract)

# Using multiply()
result_multiply = np.multiply(arr1, arr2)
print("Multiplication:", result_multiply)

# Using divide()
result_divide = np.divide(arr1, arr2)
print("Division:", result_divide)

# Using floor_divide()
result_floor_divide = np.floor_divide(arr1, arr2)
print("Floor Division:", result_floor_divide)

"""(b) Aggregate functions:
min(), max(), mean(), median(), std(), var(), percentile()
"""

import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5])

# Using min()
result_min = np.min(arr)
print("Minimum value:", result_min)

# Using max()
result_max = np.max(arr)
print("Maximum value:", result_max)

# Using mean()
result_mean = np.mean(arr)
print("Mean value:", result_mean)

# Using median()
result_median = np.median(arr)
print("Median value:", result_median)

# Using std()
result_std = np.std(arr)
print("Standard deviation:", result_std)

# Using var()
result_var = np.var(arr)
print("Variance:", result_var)

# Using percentile()
result_percentile = np.percentile(arr, 75)
print("75th percentile:", result_percentile)

"""(2) Demonstrate the Numpy Broadcasting Rules with examples of your choice"""

import numpy as np

# Creating arrays of different shapes
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])

# Broadcasting example
result = arr1 + arr2
print(result)