import time
Time = time.localtime()
t =time.strftime("Time:" "%H : %M: %S",Time)


print(t)

name = "Sai Vivek"
password = 1234
user_name = input("Enter Your Name")
user_password = int(input("Enter 4 digit password "))
Available_Balance = 50000
Time.tm_hour
if Time.tm_hour<12:
    print("Good Morning",user_name)
else:
    print("Good Evening",user_name)



if name==user_name and password==user_password:
    print(".............Welcome To Your Bank Account...............,",user_name)
    print("Choose Your Option")
    time.sleep(1.5)
    print(''' 
              1.Deposit
              2.Withdraw
              3.Change Password
              4.Exit
              5.Trnscription Script
    ''')

else:
    if name!=user_name or password!=user_password:
        print("Invalid Creditianls")
        exit()


option = int(input("Select The Option:"))
if option == 1:
        time.sleep(2)
        Deposit =int(input("Enter the amount you want to Deposit"))
        Available_Balance=Available_Balance+Deposit
        time.sleep(2)
        print("Your Total Balance is :", Available_Balance)
        time.sleep(1)
        print("Transaction Succesfully Completed")


elif option == 2:
            time.sleep(1)
            Withdraw = int(input("Enter The Amount"))
            Available_Balance = Available_Balance-Withdraw
            print("Your Total Balance is",Available_Balance)
            time.sleep(1)
            print("Transaction Succesfully Completed")

elif option==3:
        old_pin = int(input("Enter Your Old Password"))
        if old_pin ==password:

          new_pin = int(input("Enter your New pin"))
        else:
            print("Password Didnt Matched")
            time.sleep(1.5)
            print("Thank You")
            exit()

        
        """if old_pin == password:
            print("Password Matched")
        else:
            print("Password Doesnt Matched")
            exit()"""

    

        confirm = input("Confirm Y/N :")
        if confirm in ("Y","y"):
            user_password = new_pin
        print("Changing pin.........")
        time.sleep(0.5)
        print("Pin Changed Succesfully")
        password=new_pin

        if len(str(new_pin))<4:
            print("Please Enter 4 digit pin and Try again")
            exit()
        else:

            if name != user_name or password!=user_password:
              print("invalid Credintials")
            exit()
elif option ==4:
    time.sleep(0.5) 
    print("Thank You") 
elif option ==5:
    print("")              









