ch = 0
while(ch != 3):
    print("\n #################### Telephone #################### ")
    print("\n 1. Linear Probing ")
    print("\n 2. Quadratic Probing ")
    print("\n 3. Exit ")
    ch = int(input("\n Enter Your Choice : "))
    if(ch == 1):
        cho = 0
        while(cho != 4):
            print("\n 1. Read Data ")
            print(" 2. Show Data ")
            print(" 3. Search Data ")
            print(" 4. Back To Main Menu ")
            cho = int(input("\n Enter Your Choice : "))
            if(cho == 1):
                name = input("\n Enter Name : ")
                ph = int(input("\n Enter Phone No : "))
                pass
            elif(cho == 2):
                print("\n   Name is : ",name)
                print("\n   Phone No : " ,ph)
                pass
            elif(cho == 3):
                pass
            elif(cho == 4):
                break
            else:
                break
    elif(ch == 2):
        cho = 0
        while(cho != 4):
            print("\n 1. Read Data ")
            print(" 2. Show Data ")
            print(" 3. Search Data ")
            print(" 4. Back To Main Menu ")
            cho = int(input("\n Enter Your Choice : "))
            if(cho == 1):
                name = input("\n Enter Name : ")
                ph = int(input("\n Enter Phone No : "))
                pass
            elif(cho == 2):
                print("\n ----> Name is : ",name)
                print("\n ----> Phone No : ",ph)
                pass
            elif(cho == 3):
                pass
            elif(cho == 4):
                break
            else:
                break
    else:
        print("\n #################### Bye #################### ") 
            
            
