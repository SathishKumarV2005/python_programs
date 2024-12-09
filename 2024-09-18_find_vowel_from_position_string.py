def vowel(string,position):
    v=['a','e','i','o','u']
    string=string.lower()
    if position>0 and position<=len(string):
        ch=string[position-1]
        if ch in v:
            return True
        else:
            return False
    else:
        return "Invalid"

s=input("Enter the string:")
pos=int(input("Enter the position:"))

if vowel(s,pos)== "Invalid":
    print("Invalid position")
elif vowel(s,pos):
    print(f"{s[pos-1]} is a vowel")
else:
    print(f"{s[pos-1]} is not a vowel")
    
