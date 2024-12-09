'''
String and Loop - Checking for a Palindrome
Description: Write a function is_palindrome(s) that takes a string s and returns True if the string is a palindrome (reads the same forward and backward), ignoring spaces and case, and False otherwise.

Steps:
Normalize the string by converting it to lowercase and removing spaces.
Use a loop to compare characters from the beginning and end of the string moving toward the center.
Return True if all characters match, otherwise return False.
'''
def is_palindrome(str1):
    str1=str1.lower()
    str2=''
    for i in str1:
        if i !=' 'and i!='.':
            str2+=i
    str3=str2[::-1]
    if str2==str3:
        return "Palindrome"
    else:
        return "Not a Palindrome"

string=input("Enter a string:")
print("Given String is ",is_palindrome(string))
