'''
List and String - Reversing Words in a Sentence
Description: Write a function reverse_words(sentence) that takes a string sentence and returns a new string with the words in reverse order.

reverse_words("Hello World") # Output: "World Hello"
reverse_words("Python is fun") # Output: "fun is Python"

Steps:
Split the sentence into a list of words.
Reverse the list of words.
Join the reversed list back into a string.
Return the resulting string.
'''

def reverse_words(str1):
    list1=str1.split()
    list2=list1[::-1]
    newstr=' '.join(list2)
    return newstr

string=input("Enter a Sentence:")
print("The Reversed String of Words: ",reverse_words(string))
