email = input("Enter a Email: ")
k=0
j=0
d=0

if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i==i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue    
                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("Please Don't add a Space & uppercase letters in the Email")
            else:
                print("Please Enter a .")
        else:
            print("Please Enter a @")
    else:
        print("Invalid Email")
else:
    print("Oops!! Wrong Email")