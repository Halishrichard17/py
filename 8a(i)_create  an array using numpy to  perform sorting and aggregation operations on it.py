import numpy as np
a = [1,2,3,4]
#To find the aggregate sum of the array
sum = np.sum(a)
print(sum)
#output
10
#To find the minimum value in an array
min = np.min(a)
print(min)
#output
1

#To find the maximum value in the array
max = np.max(a)
print(max)
#output
4
#To find the mean value of the array
mean = np.mean(a)
print(mean)
#output
2.5
#To find the median value of the array.
med = np.median(a)
print(med)
#output
2.5
#To find the correaltion coefficiant 
cor = np.corrcoef(a)
print(cor)
#output
1
#To find the standard deviation 
std = np.std(a)
print(std)
#output
1.1180339887



#II
# Python Program illustrating
# numpy.ravel() method

import numpy as geek

array = geek.arrange(15).reshape(3, 5)
print("Original array : \n", array)

# Output comes like [ 0 1 2 ..., 12 13 14]
# as it is a long output, so it is the way of
# showing output in Python
print("\nravel() : ", array.ravel())

# This shows array.ravel is equivalent to reshape(-1, order=order).
print("\nnumpy.ravel() == numpy.reshape(-1)")
print("Reshaping array : ", array.reshape(-1))
