arr = [15, 16, 10, 9, 6, 7, 17]
arr.sort()
range = abs(arr[0] - arr[len(arr)-1])
cofficient = abs(arr[0] - arr[len(arr)-1]) / abs(arr[0] + arr[len(arr)-1])

print(cofficient)
print(range)