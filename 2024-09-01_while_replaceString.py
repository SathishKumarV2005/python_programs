#Write a program that replaces all occurrences of the old character with the new character in a given string  using a while loop.

string = input("enter the string:")
old= input("enter the old letter to replaced by new one:")
new=input("enter the Newstirng to be Filled:")
i=0
string1=""
while i<len(string):
    if string[i]==old:
        string1+=new
    else:
        string1+=string[i]
    i+=1
print("New String :",string1)