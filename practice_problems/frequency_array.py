arr = [1, 2, 3, 4, 4, 4, 5, 6, 1, 1,4]


def count_repeat(arr, key):
    repeat = {}
    for i in arr:
        if i in arr:
            repeat['i'] = arr.count(key)
    return repeat['i']


print (count_repeat(arr, 1))
