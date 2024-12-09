'''
List and Loop - Splitting and Summing Even and Odd Numbers
Description: Write a function sum_even_odd(lst) that takes a list of integers lst and returns a tuple with the sum of even numbers and the sum of odd numbers in the list.

sum_even_odd([1, 2, 3, 4, 5, 6]) # Output: (12, 9)
sum_even_odd([10, 21, 32, 43, 54]) # Output: (96, 64)

Steps:
1. Initialize two variables to store the sum of even and odd numbers.
2. Loop through the list and check if each number is even or odd.
3. Add even numbers to the even sum and odd numbers to the odd sum.
4. Return the sums as a tuple.
'''
def sum_even_odd(list1):
    sum_even=0
    sum_odd=0
    for i in list1:
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    mytuple=(sum_even , sum_odd)
    return mytuple

mylist=[int(i) for i in input("Enter list elements as integer seperated by space:").split()]
print("sum of even and odd elements in the list are ", sum_even_odd(mylist))
