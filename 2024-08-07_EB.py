units=int(input("Enter the number of units consumed:"))
if units<0:
    print("Invalid Input")
elif units<=100:
    amount=0.0
elif units<=200:
    amount=(units-100)*2.35
elif units<=400:
    amount=(100*2.35)+(units-200)*4.70
else:
    amount=(100*2.35)+(200*4.70)+(units-400)*6.30

if units>=0:
    print("Bill amount is ",amount)
