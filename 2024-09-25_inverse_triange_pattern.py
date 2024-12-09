n=int(input("enter the number of lines:"))

for i in range(n):
    for j in range(n,i,-1):
        print("*",end='')
    print()
