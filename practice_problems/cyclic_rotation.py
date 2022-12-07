arr = [7,8,9,10,11,12]
# print(arr[len(arr)-1:]+arr[:len(arr)-1])
arr2 = []
print(arr[-1:] + arr[:len(arr)-1])
for i in range(0,6):
    arr2 = arr[-1:] + arr[:len(arr)-1]
    arr = arr2


print(arr2)

