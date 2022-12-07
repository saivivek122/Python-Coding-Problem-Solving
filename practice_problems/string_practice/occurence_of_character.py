name = "This is umbrella"
repeat = {}
key1 = "e"
key2 = "is"
for i in name:
    if key1 in name:
        repeat[key1] = name.count(key1)
    if key2 in name:
        repeat[key2] = name.count(key2)
print(repeat[key1],repeat[key2])
