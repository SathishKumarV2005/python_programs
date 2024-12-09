'''
Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in the string. The function should be case-insensitive.


1. Initialize counter to keep track of the count
2. Get input string from user
3. Convert string into lower case
4. For loop to loop through characters in string
5. Create a variable list for vowels = [‘a’,e,i,o,u…]
6. Match list with every character in string
7. If matches, increment counter
8. Print vowel count
'''
string=input("Enter a string:")
count=0
vowels=['a','e','i','o','u']
string=string.lower()
for i in string:
    if i in vowels:
        count+=1
print("Number of Vowels:",count)
