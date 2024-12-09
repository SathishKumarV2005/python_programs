'''
Looping Through Lists - Removing Duplicates
Description: Write a function remove_duplicates(lst) that takes a list lst and returns a new list with duplicates removed, preserving the original order.
remove_duplicates([1, 2, 2, 3, 4, 4, 5]) # Output: [1, 2, 3, 4, 5]
remove_duplicates(["apple", "banana", "apple", "orange"]) # Output: ["apple", "banana", "orange"]

'''
def remove_duplicates(lst):
    mylist=[]
    for i in lst:
        if i not in mylist:
            mylist.append(i)
    return mylist

list1=[int(i) for i in input("Enter list elements seperated by sapce:").split() ]
print("List without Duplicate Values : ",remove_duplicates(list1))
