arr = [1, 5, 7, -1, 5]
sum = 6
count = 0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == sum:
            count+=1
print(count)