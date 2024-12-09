#Write a program  that finds and returns the largest number in a list using a while loop.



list=[int(i) for i in input("enter the list elements seperated by spaces:").split() ]
max=list[0]
i=0

while i<len(list):
    if list[i]>max:
        max=list[i]
    i+=1
print("The Largest of the list:",max)