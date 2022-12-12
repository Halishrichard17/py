import numpy as np
arr1 = np.array([1,2,3,4,5]) 
print(arr1.ndim)

#The shape Attribute

print(arr1.shape)

#The size Attribute

print(arr1.size)

#The itemsize

print(arr1.itemsize)
#The nbytes Attribute
arr2 = np.array([[1,2,3], [4,5,6]]) 
print(arr2.nbytes)