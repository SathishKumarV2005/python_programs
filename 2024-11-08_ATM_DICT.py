accounts={1:{"acc_no":1234,"PIN":"1234","name":"Ramesh","balance":30000,"branch":"palanganatham"}}
n=1


def display(acc_no,PIN):
    for key in accounts:
        if accounts[key]["acc_no"] == acc_no:
            if accounts[key]["PIN"]==PIN:
                print("Account No: ",accounts[key]["acc_no"])
                print("Name of the Account Holder:",accounts[key]["name"])
                print("Branch: ",accounts[key]["branch"])
                print("Balance:",accounts[key]["balance"])
                return
            else:
                print("Entered PIN is Wrong")
                return
    print("Account  number is not Present")



def register(acc_no,name,branch):
    global n
    n+=1
    account={}
    for key in accounts:
        if accounts[key]["acc_no"]==acc_no:
            print("Entered Account Detail is Already Exist")
            return
    account["acc_no"]=acc_no
    account["PIN"]="Not Set"
    account["name"]=name
    account["branch"]=branch
    account["balance"]=0
    accounts[n]=account
    print("Account had Registered successfully")


def PIN_Set(acc_no,PIN):
    for key in accounts:
        if accounts[key]["acc_no"] == acc_no:
            accounts[key]["PIN"]=PIN
            print("PIN Set Successful")
            return
    print("Account Number is Not Present")


def deposit(acc_no,PIN,amt):
    for key in accounts:
        if accounts[key]["acc_no"]== acc_no:
            if accounts[key]["PIN"]==PIN:
                if amt>=500 and amt<=50000:
                    accounts[key]["balance"]+=amt
                    print(f"Amount Rs. {amt} is Deposited Successfully")
                    return
                else:
                    print("Amount not in the Limit")
                    return
            else:
                print("Entered PIN is Wrong")
                return
    print("Account  number is not Present")




def withdraw(acc_no,PIN,amt):
    for key in accounts:
        if accounts[key]["acc_no"]== acc_no:
            if accounts[key]["PIN"]==PIN:
                if amt>=500 and amt<=20000:
                    if amt<=accounts[key]["balance"]:
                        accounts[key]["balance"]-=amt
                        print(f"Amount Rs. {amt} is Withdrawn Successfully")
                        return
                    else:
                        print("Insufficent Balance")
                        return
                else:
                    print("Amount not in the Limit")
                    return
            else:
                print("Entered PIN is Wrong")
                return
    print("Account  number is not Present")

    
def main():
    
    print("Menu")
    print("*"*15)
    print("\n1.Display Account Details:")
    print("2.Register a Newly Created Account")
    print("3.To Set or Change PIN:")
    print("4.To Deposit")
    print("5.To Writhdraw")
    print("6.Exit\n")
    print("*"*15)

    while True:
        choice=int(input("\nEnter the any option in the menu:"))

        if choice==1:
            acc_no=int(input("Enter the Account Number:"))
            PIN=input("Enter the PIN:")
            display(acc_no,PIN)
            
        elif choice==2:
            acc_no=int(input("Enter the Account Number:"))
            name=input("Enter the Account Holder Name:")
            branch=input("Enter the Branch of the Bank:")

            register(acc_no,name,branch)
            
        elif choice==3:
            acc_no=int(input("Enter the Account Number:"))
            PIN=input("Enter the PIN to Set or Change:")
            
            PIN_Set(acc_no,PIN)

        elif  choice==4:
            acc_no=int(input("Enter the Account Number:"))
            PIN=input("Enter the PIN:")
            amount=int(input("Enter the amount to Deposit:"))
            
            deposit(acc_no,PIN,amount)

        elif  choice==5:
            acc_no=int(input("Enter the Account Number:"))
            PIN=input("Enter the PIN to Set or Change:")
            amount=int(input("Enter the amount to Withdraw:"))
            
            withdraw(acc_no,PIN,amount)
            
        elif choice==6:
            print("Thank you")
            return

        else:
            print("Invalid Input")
            
main()     






        
