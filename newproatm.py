def withdraw(i):
    while True:
        amount = input("Enter the amount to withdraw: ")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount (i.e., an integer greater than zero).")
        except ValueError:
            print("Please enter a valid amount (i.e., an integer greater than zero).")
    pin_code=input("Enter pin:")
    if(pin_code!=pin[i]):
        print("Invalid pin")
        print("End")
    else:
        
    
        if(amount>bal[i]):
            print("Insufficient balance")
            print("EXIT")
        else:
            
            bal[i]-=amount
            print("Collect amount")
            a=input("Do you want account balance? (y/n): ")
            
            
            if a=='y':
                print("Your balance is:",bal[i])
            else:
                print("Thank you")
def deposit(i):
    amount = int(input("Enter the amount to deposit: "))
    pin_code=input("Enter pin:")
    if(pin_code!=pin[i]):
        print("Invalid pin")
        print("End")
    else:
       if amount <= 0:
          print("Invalid amount")
       else:
            bal[i] += amount
            print("Deposit successful.")
            print("Your updated balance is:", bal[i])
def balance(i):
    pin_code=input("Enter pin:")
    if (pin_code!= pin[i]):
        print("Invalid pin")
        print("End")
    else:
        print("Your current balance is:", bal[i])
def passwordchange(i):
    pin_code=input("Enter pin:")
    if(pin_code!=pin[i]):
        print("Invalid pin")
        print("End")
    special_chars = '!@#$%^&*()-_+=<>,.?/:;{}[]|\\'
    l, u, d, s = 0, 0, 0, 0  # Initialize the counting variables
    
    if len(password[i]) >= 8:
        for char in password[i]:
            if char.islower():
                l += 1
            elif char.isupper():
                u += 1
            elif char.isdigit():
                d += 1
            elif char in special_chars:
                s += 1

    while True:
        print("New password should have 8 characters,atleast 1 uppercase letter,1 lowercase letter,1 special character")
       
        new_password = input("Enter new password: ")
        confirm_password = input("Reenter the password: ")

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        if password[i] == new_password:
            print("New password must be different from the current password.")
            continue

        if password[i] == new_password:
            print("New password must be different from the current password.")
            continue

        if len(new_password) < 8:
            print("Password must have at least 8 characters.")
            continue
        
        l, u, d, s = 0, 0, 0, 0  
        for char in new_password:
            if char.islower():
                l += 1
            elif char.isupper():
                u += 1
            elif char.isdigit():
                d += 1
            elif char in special_chars:
                s += 1

        if l == 0 or u == 0 or d == 0 or s == 0:
            print("Password must have at least one lowercase letter, one uppercase letter, one digit, and one special character.")
            continue

        password[i] = new_password
        print("Password changed successfully.")
        break
   
def fun(i):
    pass_word=input("password:")
    flag=0
    if(pass_word!=password[i]):
      print("Incorrect password,you have 2 more attempts")
      pass_word=input("Enter correct password:")
      if(pass_word!=password[i]):
          print("Incorrect password,you have 1 more attempt")
          pass_word=input("Enter correct password:")
          if(pass_word!=password[i]):
              print("Incorrect password, account blocked")
          else:
              flag=1
      else:
          flag=1
    else:
        flag=1
    if flag==0:
        print("End")
    else:
        print("1.Withdraw")
        print("2.Deposite")
        print("3.Balance")
        print("4.Change Password")
        print("5.Exit")
        
        while(1):
                choice=int(input("Enter choice:"))
                if(choice in [1,2,3,4,5]):
                    break
                else:
                    print("Wrong choice, re-enter your choice:")
        if(choice==1):
           withdraw(i)
        elif(choice==2):
            deposit(i)
        elif choice == 3:
            balance(i)   
        elif(choice==4):
            passwordchange(i)
        elif(choice==5):
            print("Thank You")
            pass
user_name=['rohith','varshitha','sneha']
password=['roh12','vars22','sne44']
pin=['9080','1211','1109']
bal=[20000,16000,22000]
user=input("Enter user name:")
if user in user_name:   
      i=user_name.index(user)
      fun(i)
else:
    print("User doesn't exist")

