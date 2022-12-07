from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def searchElement(array, element):
    for i in array:
        if i == element:
            return array.index(element)
    return "the element not existed"


print(searchElement(arr1, 7))
# a = ["hari"]
# print(a[0].index("h"))
