'''
We have 3 colleges - each college has a different cut off mark for engineering college admission.Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
Condition:

 eligibility cut off of college 1 - 70%, College 2 - 80% and college 3 - 90%.

 Sample input:

 If the student's avg is, 94%, the student is eligible

Sample output:

 for admission in College 1 and College 2 and college 3

'''
mark1=int(input("Enter five Marks:"))
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

Avg = (mark1 + mark2 + mark3 + mark4 + mark5)/5

if Avg >= 90 :
    print(" you are eligibile to get admission in College1 and college 2 and College3")

elif Avg >= 80:
    print (" you are eligibile to get admission in College1 and college 2")

elif Avg >= 70:
    print (" you are eligible to get admission in college1")
    
else:
    print (" you are not eligible to get admission in the above Colleges ")



