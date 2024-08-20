from numpy import *

arr1 = array([6,3,8,9])
# arr2 = array([4,6,3,7])

# arr3 = arr1 + arr2
# print(arr3)  

# print(cos(arr1))
# print(sum(arr1))

# print(concatenate([arr1,arr2]))

arr2 = arr1

# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

# create a shallo copy use view() function
# In this array is inter connect to each other one value has change than other value is change

# arr2 = arr1.view()
# arr1[0] = 1
# print(arr1)
# print(arr2)

# print(id(arr1))
# print(id(arr2))

# create a deep copy use copy() function
# arrays are indepandes

arr2 = arr1.copy()
arr1[0] = 1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))