arr1 = [3, 2, 11, 7, 6, 5, 6, 1]
print(len(arr1))
arr2 = []
for i in range(0, len(arr1)):
    if i == len(arr1) - 1:
        arr2.append(-1)
    else:
        for j in range(i + 1, len(arr1)):
            if arr1[i] > arr1[j]:
                arr2.append(arr1[j])
                break
            elif j == len(arr1) - 1:
                arr2.append(-1)
                break
            else:
                pass
print(arr2)
