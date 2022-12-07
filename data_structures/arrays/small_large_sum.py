arr = [3, 2, 1, 7, 5, 4]

i = 0
even = []
odd = []
while i < len(arr):
    if i % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
    i+=1


sum = sorted(even)[1] + sorted(odd)[1]
print(sum)

