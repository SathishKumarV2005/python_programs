'''
String and List - Extracting Numbers from a String
Description: Write a function extract_numbers(s) that takes a string s containing both letters and numbers, and returns a list of numbers extracted from the string.
extract_numbers("abc123xyz456") # Output: [123, 456]
extract_numbers("1a2b3c") # Output: [1, 2, 3]
'''

'''

str1=input("Enter a String:")
for i in str1:
    if not i.isdigit():
     str1=str1.replace(i,' ')

list1=str1.split()
list2=[]
for d in list1:
   list2.append(int(d))

print(list2)


'''
def sep_num(str1):
    num=[]
    temp=''
    for ch in range(0,len(str1)):
        if str1[ch].isdigit():
            temp+=str1[ch]
        if not str1[ch].isdigit() and str1[(ch-1)].isdigit() and temp!='':
            num.append(int(temp))
            temp=''
    if temp!='':
        num.append(int(temp))
    print(num)

    
str1=input("Enter a string with Numbers and alphabets:")
sep_num(str1)



