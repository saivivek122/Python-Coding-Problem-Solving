arr = [8, 8, 8]


def distinct_array(arr):
    arr.sort()
    arr3 = []
    for i in arr:
        if i not in arr3:
            arr3.append(i)
    return len(arr3)


print(distinct_array(arr))
