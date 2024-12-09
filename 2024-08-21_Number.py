#print the numbers from 1 to the limit given by user

num=int(input("Enter a Number as a Limit:"))
print(f"Numbers from 1 to {num} :",end='')
for i in range(1,num+1):
    print(i, end='  ')
