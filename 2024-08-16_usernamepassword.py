username=input("Enter a username:")
password=input("Enter a password:")
prefix=(".com",".edu",".tech",".org")
if len(username)>=11 and len(password)==11:
    if  '@' not in username or not username.endswith(prefix):
        print("Invalid Username(@ or prefix is missing)")
    else:
        part1=username.split('@') #sathish@sayur.com
        part2=part1[0]
        part3=part1[1]
        if password[0] == username[0] and password[1] == username[2]: 
            if password[2:5] == part2[-3:] and password[5:8] == part3[0:3]:
                if password[8:11].isdigit():
                    print("Valid Username and Valid password")
                    print("Login successful")
                else:
                    print("Last three digits missing")
            else:
                print("Password not match with the pattern of username")
        else:
                print("Password not match with the pattern of username")
else:
    print("Invalid,Entered username or password not meet expected length")
