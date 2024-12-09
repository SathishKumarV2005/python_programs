def list_to_num(num_list):
    num=0
    power=0
    for i in num_list:
        num=num+(i*(10**power))
        power+=1
    return num

def num_to_list(num):
    num_list=[]
    while num:
        rem=num%10
        num=num//10
        num_list.append(rem)
    return num_list

mylist1=[1,2,3]
mylist2=[5,6,7]
num=list_to_num(mylist1)+list_to_num(mylist2)

newlist=num_to_list(num)
print(newlist)
