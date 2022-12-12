# importing library
import numpy

# initializing list
lst = [1, 7, 0, 6, 2, 5, 6]

# converting list to array
arr = numpy.array(lst)

# displaying list
print ("List: ", lst)

# displaying array
print ("Array: ", arr)


def solve(nums):
   for i in range(max(nums)+1):
      count=0
      for j in nums:
         if j >= i:
            count+=1
      if count == i:
         return i
      return -1

nums = [4,6,7,7,1,0]
print(solve(nums))