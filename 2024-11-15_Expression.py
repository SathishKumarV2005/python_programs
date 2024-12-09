#[{(a+b)-c}+(c+d)]


import sys
expression=input("Enter a Expression:")
mylist=[]
n=-1

for i in expression:

    if i =='[' or i == '{' or i == '(':
        mylist+=i
        n+=1

    elif i == ']' or i == '}' or i == ')':

        if mylist :
            
            if i == ']'and mylist[n] == '[':
                mylist.pop()
                n-=1
            if i == '}'and mylist[n] == '{':
                mylist.pop()
                n-=1
            if i == ')'and mylist[n] == '(':
                mylist.pop()
                n-=1
        else:
            print("Not Balanced")
            sys.exit()

if mylist == []:
    print("Given Expression is Balanced")
else:
    print("Not Balanced")
