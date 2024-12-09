#Write a program that calculates the sum of all numbers from 1 to n using a while loop.


num=int(input("Enter a number:"))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
print(sum)