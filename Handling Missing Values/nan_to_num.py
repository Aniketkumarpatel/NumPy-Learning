#np.nan_to_num(array, nan=value) default - 0

import numpy as np

arr = np.array([10, 20, np.nan, 40])

cleaned_arr = np.nan_to_num(arr,6)
print(cleaned_arr)