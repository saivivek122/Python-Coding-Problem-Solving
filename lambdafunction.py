array = [2,4,3,5,2,7,6]
for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
print(array)