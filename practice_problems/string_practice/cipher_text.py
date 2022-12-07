string = "applepine"
data = []
key = 5
j = 0
decoded = ""
for i in string:
    data.append(i)
print(data)
while key < len(data):
    decoded = decoded + data[key]
    key = key + 1
for i in range(0,len(data)-len(decoded)):
    decoded = decoded + data[i]

print(decoded)

