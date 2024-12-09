'''
Description: Write a function find_max_min(lst) that takes a list of integers lst and returns a tuple with the maximum and minimum values in the list.

find_max_min([3, 5, 1, 9, 7]) # Output: (9, 1)
find_max_min([-10, 0, 5, 12, 3]) # Output: (12, -10)


1. Get input list of integers from users
2. Initialize two variables min and max = first value of the list.  
3. Loop through list of integers
4. If current value > max , max = current_value 
5. If current value < min, min = current_value.   
6. End print max, min

'''

def find_min_max(list1):
    lstmin=list1[0]
    lstmax=list1[0]
    for i in list1:
        if i> lstmax:
            lstmax=i
        if i<lstmin:
            lstmin=i
    mytuple=(lstmin , lstmax)
    return mytuple

mylist=[int(i) for i in input("Enter the List elements as Integer Seperated by space:").split()]
print("Minimum and Maximum in the list are ",find_min_max(mylist))



