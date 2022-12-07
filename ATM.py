
import time
Time = time.localtime()
t =time.strftime("Time:" "%H : %M: %S",Time)
print(t)
Available_Balance=50000
name = "Sai Vivek"
keyword = 4568
password = 1234
user_name = input("Enter Your Name: ")
user_password = int(input("Enter 4 digit password: "))
#option = int(input("Choose Your Option"))
Time.tm_hour
if Time.tm_hour<12:
    print("Good Morning",user_name)
else:
    print("Good Evening",user_name)

    if name == user_name and password == user_password:
        print("...................Welcome To Your Bank Account...............,", user_name)
        time.sleep(1.5)
        print(''' 
                  1.Deposit
                  2.Withdraw
                  3.Change Password
                  4.Exit
                  5.Fetch Current Balance
                  6.Forget Your Password
''')
    else:
        print("Invalid Credentials")



def condition1():
    time.sleep(2)
    Deposit = int(input("Enter the amount you want to Deposit: "))
    Total_Balance=Available_Balance + Deposit
    time.sleep(2)
    print("Your Total Balance is :", Total_Balance)
    time.sleep(1)
    print("Transaction Succesfully Completed")

def condition2():
    time.sleep(1)
    Withdraw = int(input("Enter The Amount: "))
    Total_Balance = Available_Balance - Withdraw
    print("Your Total Balance is", Total_Balance)
    time.sleep(1)
    print("Transaction Succesfully Completed")

def condition3(password):
    old_pin = int(input("Enter Your Old Password"))
    if old_pin == password:

        new_pin = int(input("Enter your New pin"))
    else:
        print("Password Didnt Matched")
        time.sleep(1.5)
        print("Thank You")
        exit()
    if len(str(new_pin)) < 4:
        print("Please Enter 4 digit pin and Try again")
        exit()

    """if old_pin == password:
        print("Password Matched")
    else:
        print("Password Doesnt Matched")
        exit()"""

    confirm = input("Confirm Y/N :")
    if confirm in ("Y", "y"):
        user_password = new_pin
    print("Changing pin.........")
    time.sleep(0.5)
    print("Pin Changed Succesfully")




def condition4():
    print("Thank you")
    time.sleep(1.5)


    exit()
def condition5():
    print("Fetching Balance...........")
    time.sleep(1.5)
    print("Your Account Balance is",Available_Balance)


def condition6():
   Entered_keyword = int(input("Please Enter Your Keyword"))
   if keyword==Entered_keyword:
        new_password=int(input(("Enter Your New Password")))
        time.sleep(1.5)
        print("Password Changed Succesfully")
        new_password=password
   else:
    time.sleep(1.5)
    print("Keyword Didnt Matched")




option = int(input("Chosse Your Option"))

if option ==1:
    condition1()
elif option==2:
    condition2()
elif option ==3:
    condition3(password)
elif option ==4:
    condition4()
elif option ==5:
    condition5()
elif option ==6:
    condition6()





























