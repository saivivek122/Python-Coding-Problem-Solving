first = int(input("first"))
second = int(input("second"))
if first < second:
    smaller = first
else:
    smaller = second
for i in range(1,smaller+1):
    if first % i == 0 and second % i == 0:
        hcf = i
print(hcf)