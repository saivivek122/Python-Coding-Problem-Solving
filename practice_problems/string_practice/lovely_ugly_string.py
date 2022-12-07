n = int(input())
vowel = set("aeiou")
data = []
data2 = []
for j in range(0,n):
    data2.append(input())
for i in data2:
    for k in i.lower():
        if k in vowel and k not in data:
            data.append(k)
    print(data)
    if len(data) == 5:
        print('lovely string')
    else:
        print("ugly string")



