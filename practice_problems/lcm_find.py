first = int(input("first"))
second = int(input("second"))
if first > second:
    greater = first
else:
    greater = second
while(True):
    if greater % first == 0 and greater % second ==0:
        lcm = greater
        break
    greater+=1
print(lcm)