import os
from op_ovr import *
os.system('clear')
ov1=Operators1()
ov2=Operators1()
ov1.accept()
ov2.accept()

while True:
    print("1 : overloading + operator")
    print("2 : overloading - operator")
    print("3 : overloading * operator")
    print("4 : overloading // operator")
    print("5 : exit")
    print("*"*100)
    c=int(input("Enter your choice : "))
    if c == 1:
        print(ov1+ov2)
    elif c == 2:
        print(ov1-ov2)
    elif c == 3:
        print(ov1*ov2)
    elif c == 4:
        print(ov1//ov2)
    elif c == 5:
        break
    else:
        print("invalid entry")
