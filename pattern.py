'''

A
b C
D e F
g H i J

'''

pattern="ABCDEFGHIJ"
n=0
for i in range(0,4):
    for j in range(0,i+1):
        if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
            print(pattern[n],end=' ')
            n+=1
        else:
            print(pattern[n].lower(),end=' ')
            n+=1
    print()
