#set operations
a={1,2,3,4}
b={5,1,4,6}
while True:
    print("1: add elements ")
    print("2: copy set ")
    print("3: length of set ")
    print("4: maximum element")
    print("5: union operarion ")
    print("6: intersection operation")
    print("7: difference operation")
    print("8: symmetric difference")
    print("9: issubset operarion")
    print("10: issuperset operation")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        n = int(input("Enter the element to be add : "))
        a.add(n)
        print("the set after adding elements : ",a)
    elif ch == 2:
        c=a.copy()
        print("The copied set : ",c)
    elif ch == 3:
        print("the length of a set : ",len(a))
    elif ch == 4:
        print("Maximium element in set : ",max(a))
    elif ch == 5:
        print("The union of ",a," and ",b," is : ",a.union(b))
    elif ch == 6:
        print("The intersection of ",a," and ",b," is : ",a.intersection(b))
    elif ch == 7:
        print("The difference of ",a," and ",b," is : ",a.difference(b))
    elif ch == 8:
        print("The symmentric difference of ",a," and ",b," is : ",a.symmetric_difference(b))
    elif ch == 9:
        print(a," is subset of ",b," : ",a.issubset(b))
    elif ch == 10:
        print(a," is superset of ",b," : ",a.issuperset(b))
    else:
        print("Invalid choice !!")
