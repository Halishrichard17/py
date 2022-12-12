import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(f'Original Array:\n{arr1}')

a = arr1.transpose()

print(f'Transposed Array:\n{a}')


print(a)
b = 3
print(b)

# Broadcasting happened because of
# miss match in array Dimension.
c = a + b
print(c)
