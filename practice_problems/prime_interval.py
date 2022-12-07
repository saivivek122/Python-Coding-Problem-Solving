s = int(input("enter starting"))
e = int(input("enter ending"))
def prime_range_interval(s,e):
    arr = []
    for i in range(s+1,e):
        if i % 2 != 0:
            arr.append(i)

    return arr
print(prime_range_interval(s,e))
