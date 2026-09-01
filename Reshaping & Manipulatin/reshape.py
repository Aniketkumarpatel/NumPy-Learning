"""
reshape(rows, columns) specify new shpe
if dimensions match
"""

import numpy as np

arr = np.array([10,20,30,50,40,80,90,70])
print(arr)
reshaped_Arr = arr.reshape(2,4)
print(reshaped_Arr)