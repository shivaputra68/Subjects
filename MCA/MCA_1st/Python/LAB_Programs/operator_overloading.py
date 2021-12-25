from magic_methods import *
o1 = Operation()
o2 = Operation()
while True:
    print("1: addition ")
    print("2: subtraction ")
    print("3: Multiplication ")
    print("5: floor division ")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print(o1+o2)
    elif ch == 2:
        print(o1-o2)
    elif ch == 3:
        print(o1 * o2)
    elif ch == 5:
        print(o1 // o2)
    else:
        pass
