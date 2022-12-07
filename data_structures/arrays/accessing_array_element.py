from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])


def accessArray(array, index):
    if index >= len(array):
        print("error")
    else:
        print(array[index])


accessArray(arr1, 6)
