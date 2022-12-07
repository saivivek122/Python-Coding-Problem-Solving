num = int(input("enter a number"))
flag = False
for i in range(2,num):
    if num % i == 0:
        flag = False
        break
    else:
        flag = True
if flag:
    print("prime")
else:
    print("not")
