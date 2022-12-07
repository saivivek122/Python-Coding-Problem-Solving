arr = [1, 2, 4, 6, 3, 7, 8]
k = max(arr)
j = 1
for i in range(0,len(arr)):
    if j not in arr:
        print(j)
    j+=1


