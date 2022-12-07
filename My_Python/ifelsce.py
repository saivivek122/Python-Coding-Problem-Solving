# a = int(input("enter number"))
# if a >= 0:
#     print("positive")
# else:
#     print("negative")
a = int(input("enter first"))
b = int(input("enter second"))
c = int(input("enter third"))
if a>b and a>c:
    print(c)
elif b>a and b>c:
    print(b)
else:
    print(c)