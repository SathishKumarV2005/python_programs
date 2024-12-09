stack=[]
n=0
option=0

size=int(input("Enter the size of the stack:"))
      
while option!=5:
    print("\tMenu\n","*"*15,"\n1.Push\n2.Pop\n3.Top\n4.Display Stack\n5.Exit\n","*"*15,"\n")
    option=int(input("Enter any option above Mentioned:"))

    if option==1: #push
        
        if n<size: #isfull
            ele=int(input("Enter The Element to Push:"))
            stack.insert(0,ele)
            print(ele," is pushed into the  stack successfully")
            n+=1
        else:
            print("Stack is Already Full")
            
    elif option==2: #pop
        
        if n!=0:
            
            print(stack[0]," is poped successfully")
            del stack[0]
            n-=1
            
        else:
            print("Stack is Already Empty")
            
    elif option==3:
        
        if n!=0:
            print(stack[0]," is the Top of the list")
        else:
            print("Stack is Empty")

    elif option==4:

        if n!=0:
            
            print("\tStack Elements:\n")
            
            for ele in stack:
                print("\t",ele)
            print()
        else:
            print("Stack is Empty")        
    elif option==5:
        
        print("System is Exiting....")
        break

    else:
        print("Invalid Input Enter option correctly")
        
