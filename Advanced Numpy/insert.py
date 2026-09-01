"""
np.insert(array, index, value, asix=None)
array - original array
index - 
value - 
axis -
axis = 0, row-wise
1 column wise
"""

import numpy as np

arr= np.array([1,2,3,4,5,6])
print(arr)
new_arr = np.insert(arr, 2,100)
print(new_arr)