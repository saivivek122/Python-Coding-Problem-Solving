from array import *

arr1 = array('i', [1, 2, 3, 4, 5])


# arr1.remove(1)
# print(arr1)

def delete_element(array, element):
    array.remove(element)
    print(array)


delete_element(arr1, 1)
