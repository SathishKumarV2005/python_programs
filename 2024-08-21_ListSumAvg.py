#to find the sum and average of marks in list

marks=[int(m) for m in input("Enter the marks separated by spaces: ").split()]

sum1=0

for k in marks:
    sum1+=k

print(f"Sum of Entered Marks is {sum1}")

avg=sum1/10
print(f"Average of Entered Marks is {avg}")
