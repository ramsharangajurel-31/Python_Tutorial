# checking the data types
import numpy as np

arr=np.array([1,2,3])
print(arr.dtype)

# changing the data types
arr=np.array([1.5,2.3,3.6,4.7])
int_arr=arr.astype(np.int32)
print(int_arr)