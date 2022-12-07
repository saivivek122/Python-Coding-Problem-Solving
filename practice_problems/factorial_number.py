number = int(input("enter number"))
factorial = 1
if number < 0:
    print("no fact for -ve")
elif number == 0:
    print("fact os zero in 1")
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print(factorial)