arr = [1, 2, 3, 4, 56, 11, 12]
temp = 0

def sorting_array(arr):
    arr.sort(reverse=True)  # by default sort will done by asc
    return arr


print(sorting_array(arr))
# using for loop
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)


