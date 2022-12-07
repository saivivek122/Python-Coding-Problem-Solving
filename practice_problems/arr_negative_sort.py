arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# arr.sort()
# print(arr)
# using quick sort
j = 0
for i in range(0,len(arr)):
    if arr[i] < 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j = j + 1
print(arr)
