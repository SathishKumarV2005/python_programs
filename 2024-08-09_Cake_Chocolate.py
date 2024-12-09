#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.
#find how many choc and cake the user can buy.


cake_avail=int(input("Enter the number of cakes in the shop:"))
choc_avail=int(input("Enter the number of chocolates in the shop:"))
budget=int(input("Enter the budget you have to buy:"))
cake_count=0
choc_count=0
initial=budget

preferred=int(input("Enter the food number you are going buy at first: \n 1.Cake \n 2.Chocolate"))

while budget>=150:
    
    if cake_avail<=0 and choc_avail<=0:
        print("Sorry all of our stocks are now Out of stock\n")
        break
    
    elif preferred==1:
        
        if cake_avail>=1:
            
            cake_count+=1
            cake_avail-=1
            budget-=150
            print(f"you bought {cake_count} cake\n")
            
            if choc_count>=1:
                print(f"you bought {choc_count} chocolate\n")
                
        else:
            
            print("Sorry cake is not available.you can buy chocolate\n") 
    
    elif preferred==2:
        
        if choc_avail>=1:
            
            choc_count+=1
            choc_avail-=1
            budget-=200
            print(f"you bought {choc_count} chocolate\n")    
            
            if cake_count>=1:
                print(f"you bought {cake_count} cake\n")
       
        else:
            
            print("sorry chocolate is not available.you can buy cakes\n")
            
    else:
        
        print("Entered input is wrong\n")
    
    preferred=int(input("Enter the food you are going to buy next: \n 1.Cake \n 2.Chocolate")) 
     
else:
    print("your budget is low\n")
    
if initial>=150:
    print(f"Total cakes you bought are {cake_count}")
    print(f"Total chocolate you bought are {choc_count}\n")
    print(f"Remaining amount you have is {budget}")
    print(f"Amount of purchase is {initial-budget}")
