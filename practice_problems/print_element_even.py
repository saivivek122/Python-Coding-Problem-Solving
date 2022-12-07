arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_even(arr):
    data = []
    i = 1
    while i < len(arr):
        data.append(arr[i])
        i += 2
    return data


k = print_even(arr)
print(k)
