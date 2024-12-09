#Write a program that removes all spaces from a given string s using a while loop.


str1=input("Enter a string:")
index=0
str2=""
print("hello")
while index<len(str1):
    if str1[index] != " ":
        str2+=str1[index]
    index+=1
print(f"String without spaces: {str2}")
