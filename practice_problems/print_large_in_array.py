arr = [25,7,77,98]
print(max(arr))
#with for loop
max = arr[0]
for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
