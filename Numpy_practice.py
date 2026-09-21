import numpy as np
import math

a = np.array([1,2 ,3 ,4 ,5, 6])
b =  a[:3]
b[2] = 67
print(b)
print(a)

mulArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(mulArray)
print(mulArray[2, 3])
print(mulArray.ndim)
print(mulArray.shape)
print(len(mulArray.shape) == mulArray.ndim)
print(mulArray.size)
print(mulArray.size == math.prod(mulArray.shape))
print(mulArray.dtype)

print(np.zeros(10))
emptArr = np.empty(10)
value = 0
for i in range(len(emptArr)):
    value += 1
    emptArr[i] = value
print(emptArr)

print(np.arange(0, 20, 10))
print(np.linspace(0, 20, 10, dtype=np.int64))
print(np.linspace(0, 1, 100))

artToSort = np.arange(11, 1, -1)
print(np.sort(artToSort))

# this is to concatinate between same axes arrays 2 + 2
x = np.array([[1,2], [3,4]])
y = np.array([[5,6]])
print(np.concatenate((x, y), axis=0))

# this is to concatinate between different axes arrays. 2 + 1
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([5,6])
print(np.vstack((arr1, arr2)))

arr3 = np.array([[1,2], [3,4]])
arr4 = np.array([[5], [6]])
print(np.concatenate((arr3, arr4), axis=1))