arr = [1,2,3,34,45,65]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)