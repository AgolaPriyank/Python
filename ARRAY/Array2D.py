# for create the 2D array we import numpy package 

from numpy import *

# arr = array([5,9,3,7,55,6],int) 
# print(arr.dtype)


# arr = linspace(0,15,16)
# print(arr)

# arr = arange(1,20,3)
# print(arr)


# arr = logspace(1,40,10)
# print(arr)

# arr = zeros(5)
# print(arr)


# arr = ones(5,int)
# print(arr)

# arr = array([
#         [1,2,3,1],
#         [4,5,6,4],
#         [7,8,9,5]
# ])

# print(arr)
# print(arr.ndim)
# print(arr.shape)

# arr2 = arr.flatten()
# print(arr2.size)

# arr3 = arr2.reshape(3,2,2)
# print(arr3)


# m = matrix(arr)
# print(m)

m1= matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
# print(m)
# print(diagonal(m))
# print(max(m))

m3 = m1+m2;
print(m3)

m4 = m1-m2;
print(m4)

m5 = m1*m2;
print(m5)