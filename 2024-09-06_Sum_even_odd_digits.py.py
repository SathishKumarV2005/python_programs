#find the sum of even and odd digits given by user

num=int(input("Enter a number:"))

if num<0:
    num=-num
    
count=0
count_even=0
count_odd=0

sum1=0
sum_even=0
sum_odd=0

while num>0:
    
    temp=num%10
    num=num//10
    sum1+=temp
    count+=1
    
    if temp%2==0:
        sum_even+=temp
        count_even+=1
    else:
        sum_odd+=temp
        count_odd+=1
        
print("count of digits:",count)
print("count of  even digits:",count_even)
print("count of  odd digits:",count_odd)
print("sum of digits:",sum1)
print("sum of even digits:",sum_even)
print("sum of odd digits:",sum_odd)


