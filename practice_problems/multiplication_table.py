number = int(input("enter number for multiply"))
ranges = int(input("enter range for multiplication"))
def multiply(number,range):
    arr = []
    for k in range(0,ranges+1):
        result = number * k
        arr.append((str(number)+'*'+str(k)+"="+str(result)))
    return arr
k = multiply(number,range)
for i in k:
    print(i)
