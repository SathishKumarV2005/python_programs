#to check the web address is valid or not

web=input("Enter the site address:")
web=web.lower()
temp=web.split('.')
intial=("http://www.","https://www.","www.")
end=(".com",".edu",".gov.in",".org",".tech")
if web.startswith(intial) and web.endswith(end) and len(temp)>=3 :
    for i in range(1,len(temp)-1):
         if  not temp[i].isalnum():
             print("Invalid web Address")
             break
    else:
        print("Valid Web address") 
else:
    print("Invalid Web address")
