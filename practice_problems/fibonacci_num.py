numbers = int(input("enter how many you want"))
n1 = 0
n2 = 1
count = 2
if numbers <= 0:
    print("enter a valid ")
elif numbers == 1:
    print("fibonacci:")
    print(n2)
else:
    print("fibonacci:")
    print(n1,n2,end=',')
    while count < numbers:
        nth = n1 + n2
        print(nth,end=",")
        n1 = n2
        n2 = nth
        count+=1