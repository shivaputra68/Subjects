#Tuple operations
t = (1,2,1,3,1,4,5)
t1 = ('r','@',1.02)
while True:
    print("1: concatinating tuples")
    print("2: count elements ")
    print("3: get index ")
    print("4: check elements")
    print("5: length of tuple")
    print("6: largest element")
    print("7: repeatation")
    print("8: range slice")
    print("9: slice ")
    print("10: delete")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("concatinated tuple ",t+t1)
    elif ch == 2:
        c = int(input("Enter the element to be count "))
        print("The element",c," in ",t," : ",t.count(c))
    elif ch == 3:
        c = int(input("Enter the value : "))
        print("The value ",c," is at ",t.index(c))
    elif ch == 4:
        c=int(input("Enter the value "))
        print("The value",c," in ",t," : ",c in t)
    elif ch == 5:
        print("the length of the tuple : ",len(t))
    elif ch == 6:
        print("The highest element in ",t," is : ",max(t))
    elif ch == 7:
        print("The ",t," repetions : ",t*2)
    elif ch == 8:
        m=int(input("Enter the starting point : "))
        n=int(input("Enter the ending point : "))
        t2 = t[m:n]
        print("the sliced tuple : ",t2)
    elif ch == 9:
        c=int(input("Enter the idex value :"))
        print("The element at ",c," is : ",t[c])
    elif ch == 10:
        del t
    else:
        print("invalid entry !!")
