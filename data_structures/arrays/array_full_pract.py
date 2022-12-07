from array import *
# 1. create and traverse aray
arr1 = array('i', [1, 2, 3, 4, 5])
for i in arr1:
    print(i)
# 2. use of insert function
#insert(index,value)
arr1.insert(0,22)
print(arr1)
# usage of extend function
arr2 = array('i', [10,11,12,13,14])
arr2.extend(arr1)
print(arr2)
#adding items from list to array
print(arr2.index(1))
print(arr1.buffer_info())



