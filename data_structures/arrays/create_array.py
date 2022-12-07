from array import *


arr1 = array('i',[1,2,3,4,5])
#print(arr1)
 # insert at end
arr1.insert(6,6)
#print(arr1)
# insert at beginning
arr1.insert(0,0)
#print(arr1)
#Travaersing operation

def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr1)
