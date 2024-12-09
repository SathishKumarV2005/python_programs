'''
Ask 4 digit Pin number before asking needed cash.
If entered pin was correct, Then ask amount and Proceed further steps that you already know.
If entered pin wasn't correct, say "wrong pin" and ask the pin again (up to 3 times)
If pin entered as incorrect for 3 times, Say "Transaction Failed, Exceeded maximum pin attempts" for the current user and (Loop will be continued) Ask pin number for the next user.
Continue the loop until Cash_in_machine=0.
'''

db_pin=[1234,2345,3456,4567,5678,6789]
db_name=["sathish","santhosh","dinesh","rajesh","ramesh","rakesh"]
budget=100000

while budget>0 :

    name=input("Enter your name:")
    name=name.lower()

    if name in db_name:
        print(f"Hi Welcome {name}")

        for j in range(3):
            pin=int(input("Enter the PIN:"))
            i=db_name.index(name)

            if pin==db_pin[i]:
                amount=int(input("Enter the amount do you want to Withdraw:"))

                if budget>=amount:
                    if amount>=500: 
                        if amount<=25000:
                            budget-=amount
                            print(f"Collect your cash of {amount} Rs")
                            print(f"Thank you {name}")
                        else:
                            print("Entered amount Is beyond the Limit of withdrawl")
                    else:
                        print("Entered amount is lesser than minimum cash withdrawl")  
                else:
                    print("Insufficeint Cash In ATM. you can try lesser amount")
                break
            else:
                if (2-j) !=0:
                    print(f"Wrong Pin number. you have {2-j} attempts remaining ")
        else:
            print("wrong pin number.Limit reached")

    else:
        print("User Name not Exist")
else:
    print("ATM is running out of cash")