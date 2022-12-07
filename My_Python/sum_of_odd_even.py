a = [10, 11, 7, 12, 14]


def findOddEvenDifferencs(size, array):
    even = []
    odd = []
    i = 0
    while i < size:
        if (a[i]%2)== 0:
            even.append(a[i])
        else:
            odd.append(a[i])
        i = i + 1
    even = sum(even)
    odd = sum(odd)
    print(odd-even)


findOddEvenDifferencs(5, a)


