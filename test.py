# your code here
data = input()
array = input()
count = 0
data = list(map(int,data.split()))
array = list(map(int,array.split()))

for i in range(data[0]):
    for j in range(i+1 , data[0]):
        if (array[i] - array[j]) == data[1]:
            count+=1
        elif (array[j] - array[i]) == data[1]:
            count+=1
print(count)
