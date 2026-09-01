"""
Simple Difference
.ravel() → usually returns a view of the original array.
.flatten() → always returns a copy of the original array.
"""

import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())