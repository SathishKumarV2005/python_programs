queue=[]
n=0
option=0

size=int(input("Enter the size of the Queue:"))
      
while option!=6:
    print("\n\tMenu\n","*"*15,"\n1.Enqueue\n2.Dequeue\n3.Front\n4.Rear\n5.Display All\n6.Exit\n","*"*15,"\n")
    option=int(input("Enter any option above Mentioned:"))

    if option==1: #Enqueue
        
        if n<size: #isfull
            ele=int(input("Enter The Element to Enqueue:"))
            queue.append(ele)
            print(ele," is Enqueued successfully")
            n+=1
        else:
            print("Queue is Already Full")
            
    elif option==2: #dequeue
        
        if n!=0: #isempty
            
            print(queue[0]," is Dequeued successfully")
            del queue[0]
            n-=1
            
        else:
            print("Queue is Already Empty")
            
    elif option==3: #Front
        
        if n!=0:
            print(queue[0]," is the Front of the queue")
        else:
            print("Queue is Empty")

    elif option==4: #Rear

        if n!=0:
            print(queue[n-1]," is the rear of the queue")
        else:
            print("Queue is Empty")


    elif option==5: #Display Queue
        
        if n!=0: 
            print("\tQueue Elements:\n")
            print(end="\t  ")
            
            for ele in queue:
                print(ele,end=" ")
        else:
            print("Queue is Empty")
        print()
            
    elif option==6: #exit
        
        print("System is Exiting....")
        break

    else:
        print("Invalid Input Enter option correctly")
        
