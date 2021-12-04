import time
ch=int(input("Enter your choice from 1 to 8\n"))
a = time.time()
if ch==1:
    print("The Choice is 1 ")
elif ch==2:
    print("The Choice is 2 ")
elif ch==3:
    print("The Choice is 3 ")
elif ch==4:
    print("The Choice is 4 ")
elif ch==5:
    print("The Choice is 5 ")
elif ch==6:
    print("The Choice is 6 ")
elif ch==7:
    print("The Choice is 7 ")
elif ch==8:
    print("The Choice is 8 ")
else:
    print("This is always printed ")
b = time.time()
print("Time == ",b-a)
    
        
