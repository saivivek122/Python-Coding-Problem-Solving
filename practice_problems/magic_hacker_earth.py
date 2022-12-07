n = int(input())
data = input()
data = data.split()
data2 = []
data3 = []
data4 = []
flag = 0
for i in data:
    data2.append(int(i))
k = sum(data2)
j = 0
for i in data2:
    if (k - int(i)) % 7 == 0:
        data3.append(i)

if len(data3) == 0:
    print("-1")
else:
    p = min(data3)
x = 0
while x < len(data2):
    if data2[x] == p:
        print(x)
        break
    else:
        x+=1