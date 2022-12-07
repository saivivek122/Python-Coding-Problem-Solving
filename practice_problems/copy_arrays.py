arr1 = [1,2,3,4]
arr2 = []
arr2 = arr1[:]
print(arr2)
# methos 2
arr2 = arr1
print(arr2)
#methd 3
arr2 = arr1.copy()
print(arr2)
arr2 = []
for i in arr1:
    arr2.append(i)
print(arr2)