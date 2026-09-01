"""
slicing
array[start: stop: step]

arr[start:end],   start to ned-1

negative step, -1 reverse
"""

import numpy as np

arr = np.array([12,124,34,45,56,55,22,11,10])
print(arr)
print(arr[1:5]) # index 1 to 4
print(arr[:4]) # index 0 to 3
print(arr[::2])
print(arr[::-1])