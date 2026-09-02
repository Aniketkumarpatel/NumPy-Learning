
import numpy as np

arr = np.array([10, 20, np.inf, 40])

print(np.isinf(arr))

cleand_arr = np.nan_to_num(arr,posinf=1000)
print(cleand_arr)