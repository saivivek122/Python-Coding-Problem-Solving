import re
password = "123"
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        break
    elif not re.search("[a-z]",password):
        flag = -1
        break
    elif not re.search("[A-Z]",password):
        flag = -1
        break
    elif not re.search("[0-9]",password):
        flag = -1
        break
    elif not re.search(("[_@$]"),password):
        flag = -1
        break
    else:
        flag = 0
        print("valid")
        break
if flag == -1:
    print("in valid")
