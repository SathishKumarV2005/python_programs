#Write a program  that calculates the factorial of a given number n using a while loop.

fact=1
num=int(input("Enter a number:"))
i=1
while i<=num:
    fact=fact*i
    i+=1
print(f"Facotial of the given Number is {fact}")    