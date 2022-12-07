number = int(input("ente number to check"))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = int(temp / 10)
if sum == number:
    print("yes")
else:
    print("no")
