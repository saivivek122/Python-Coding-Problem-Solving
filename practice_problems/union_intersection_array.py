arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
i = 0
# while i < len(arr1):
#     if arr1[i] not in arr2:
#         arr2.append(arr1[i])
#     i += 1
# arr2.sort()
# print(arr2)
# intersection
arr3 = []
if len(arr1) > len(arr2):
    check = arr1
else:
    check = arr2
j = 0
while j < len(check):
    print(check[j])
    if (check[j] in arr1) and (check[j] in arr2):
        arr3.append(check[j])
    j += 1
print(arr3)
