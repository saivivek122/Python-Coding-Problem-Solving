arr1 = [1, 2, 3, 4, 5, 6]


def count_outcomes(arr1, sum):
    i = 0
    count = 0
    while i < len(arr1):
        j = 0
        while j < len(arr1):
            if arr1[i] + arr1[j] == sum:
                count += 1
                j += 1
            else:
                j += 1
        i += 1
    return count


print(count_outcomes(arr1, 100))
