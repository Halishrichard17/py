# importing the module
from numpy import *                  
 
# creating the first array
arr1 = array([2, 6, 9, 4])            
 
# displaying the identity of arr1
print(id(arr1))
 
# assigning arr1 to arr2
arr2 = arr1                         
 
# displaying the identity of arr2
print(id(arr2))
 
# making a change in arr1
arr1[1] = 7                        
 
# displaying the arrays
print(arr1)
print(arr2)