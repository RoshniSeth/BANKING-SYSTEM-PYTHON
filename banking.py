import random as r
import os
import json
import time

print("\t\t\t","Welcome to Yes Bank")
print()
print("-"*70)
print()
print("Select the Preferred Option")
print()

options=["1.Open Account","2.Deposit Cash","3.Cash Withdrawal","4.Check Balance","5.Quit"]
for i in options:
    print(i)
print()   
print("-"*70)
print()
print()

customer_details={}


cwd=os.getcwd()                                     
file_name="customer_records.txt"                        
file_path=os.path.join(cwd,file_name)

def file_data():
    global file_name,file_path
    if os.path.exists(file_path)==True:     
        f=open(file_path,"r")                         
        data=f.read()                                 
        consumer_details=json.loads(data)             
    else:
        f=open(file_path,"w+")
        consumer_details={}
        f.close()
    return consumer_details



        
def open_account():
    global customer_details
    
    name=input("enter your full name: ")
    for i in name:
      while not (i.isalpha() or i.isspace()):
         print("Invalid Name Entered")
         print()
         name=input("Enter Your Full Name: ")
         
    aadhaar_number=input("enter your aadhaar card number(12-digit): ")
    while len(aadhaar_number)!=12 or not(aadhaar_number.isdigit()):
        print("Invalid Aadhaar Number Entered")
        print()
        aadhaar_number=input("Enter Your Mobile Number(10-digit): ")
        
    email_id=input("Enter Your Email Address: ")
    while "@" not in email_id or not email_id.endswith(".com"):
            print("Invalid Email Address Entered")
            print()
            email_id=input("Enter Your Email Address: ")


    mobile_number=input("enter your mobile number(10-digit): ")
    while len(mobile_number)!=10 or not(mobile_number.isdigit()):
        print("Invalid Mobile Number Entered")
        print()
        mobile_number=input("Enter Your Mobile Number(10-digit): ")
   
    
    account_number=r.randint(10000001,99999999)
    account_number=str(account_number)
    
    
    while account_number in customer_details.keys():
        print("account number already exists")
        account_number=r.randint(10000001,99999999)
        
    customer_details[account_number]={"Name":name,"aadhaar number":aadhaar_number,"Balance":0,"mobile_number":mobile_number,"email address":email_id}

    print()
    time.sleep(1)
    print()
    print("Congrats!Your account has been created.")
    print("Your account number is: ",account_number)
    print("Your name is: ",name)
    print("Your current balance is:Rs  ",customer_details.get(account_number).get("Balance"))


    print()
    print("-"*70)

def deposit_cash():
    global customer_details
    print()
    user_input=input("Enter Your Account Number: ")
    while user_input not in customer_details.keys():
            time.sleep(1)
            print()
            print("Invalid Account Number Entered.")
            print("Please entered a valid account number.")
            print()
            user_input=input("Enter Your Account Number: ")
    print()
    amount=float(input("Enter the amount to be deposited: "))

    new_amount=customer_details.get(user_input).get("Balance")+amount
    customer_details[user_input]["Balance"]=new_amount
    print()
    time.sleep(1)
    print("Available balance in Account: ",customer_details.get(user_input).get("Balance"))
    print()

    print("-"*70)
    print()

    
def cash_withdrawal():
    global customer_details
    print()
    user_input=input("Enter Your Account Number: ")
    while user_input not in customer_details.keys():
            time.sleep(1)
            print()
            print("Invalid Account Number Entered.")
            print("Please entered a valid account number.")
            print()
            user_input=input("enter your account number: ")
    print()
    amount=float(input("Enter the amount to be withdrawn: "))
    while customer_details.get(user_input).get("Balance")<amount:
        time.sleep(1)
        print()
        print("Not Enough Balance In Account")
        print("Available balance in Account: ",customer_details.get(user_input).get("Balance"))
        print()
        amount=float(input("enter the amount to be withdrawn: "))
        

    new_amount=customer_details.get(user_input).get("Balance")-amount
    customer_details[user_input]["Balance"]=new_amount
    print()
    time.sleep(1)
    print("Available balance in Account: ",customer_details.get(user_input).get("Balance"))
    print()

    print("-"*70)
    print()

def check_balance():
    global customer_details
    print()
    user_input=input("Enter Your Account Number: ")
    while user_input not in customer_details.keys():
            print()
            time.sleep(1)
            print("Invalid Account Number Entered.")
            print("Please entered a valid account number.")
            print()
            user_input=input("enter your account number: ")
    print()
    time.sleep(1)
    print("Name                       ",customer_details[user_input]["Name"])
    print("Registered Email           ",customer_details[user_input]["email address"])
    print("Registered Mobile Number   ",customer_details[user_input]["mobile_number"])
    print("Available Balance          ",customer_details[user_input]["Balance"])
    print()
    print("-"*70)
    print()

file_dataaa = file_data()                       
customer_details = file_dataaa                                              
        
def bank(customer_details):
    while True:
        valid_options=["1","2","3","4","5"]
        user_option=input("Enter the required option: ")
        while user_option not in valid_options:
            time.sleep(1)
            print("Invalid option entered.")
            print("Please enter the valid option.")
            print()
            user_option=input("Enter the required option: ")
            
        user_option=int(user_option)
        
        if user_option==5:
            print("Thank You For Using Yes Bank!")
            file = open(file_path, 'w')
            file.writelines(json.dumps(customer_details))
            file.close()
            break
        else:
          if user_option==1:
            open_account()
          elif user_option==2:
            deposit_cash()
          elif user_option==3:
            cash_withdrawal()
          elif user_option==4:
            check_balance()

bank(customer_details)
            

        

