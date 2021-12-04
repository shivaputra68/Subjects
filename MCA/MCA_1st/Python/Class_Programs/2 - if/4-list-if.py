import time
ch=int(input("Enter your choice from 1 to 8\n"))
a = time.time()
if ch==1:
    print("The Choice is 1 ")
if ch==2:
    print("The Choice is 2 ")
if ch==3:
    print("The Choice is 3 ")
if ch==4:
    print("The Choice is 4 ")
if ch==5:
    print("The Choice is 5 ")
if ch==6:
    print("The Choice is 6 ")
if ch==7:
    print("The Choice is 7 ")
if ch==8:
    print("The Choice is 8 ")
else:
    print("This is always printed ")
b = time.time()
print("Time == ",b-a)
    
        
