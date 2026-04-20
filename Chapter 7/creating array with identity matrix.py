# creating array with identity matrix
# creating a 3*3 matrix
import numpy as np
identity_matrix=np.eye(3)
print(identity_matrix)
# creating array with custom data types
array_int=np.array([1,2,3,4],dtype=np.int32)
print(array_int)
array_float=np.array([1,2,3,4],dtype=np.float64)
print(array_float)
# creating an array without initializing the values(contains arbitrary values)
empty_array=np.empty((2,3))
print(empty_array)

