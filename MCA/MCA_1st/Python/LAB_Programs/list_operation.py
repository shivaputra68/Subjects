#List operations
a = [1,5,2,7,3,4,6]
b = [3,4]
while 1:
    print("1: add items")
    print("2: concatinate list")
    print("3: length ")
    print("4: max value ")
    print("5: sort list")
    print("6: pop element ")
    print("7: remove element")
    print("8: reverse list")
    print("9: copy list")
    print("10: delete list")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        c = int(input("Enter the item to be inserted : "))
        a.append(c)
        print("List after inserted : ",a)
    elif ch == 2:
        print("The concatinated list : ",a+b)
    elif ch == 3:
        print("The length of the list : ",len(a))
    elif ch == 4:
        print("The maximum value in list ",a," is : ",max(a))
    elif ch == 5:
        a.sort()
        print("the sorted list ",a)
    elif ch == 6:
        print("removing last item in list : ",a.pop())
        print("list after poped elements : ",a)
    elif ch == 7:
        c=int(input("Enter the element to be removed : "))
        a.remove(c)
        print("The list after removing ",c," is",a)
    elif ch == 8:
        a.reverse()
        print("reverse order list : ",a)
    elif ch == 9:
        c=a.copy()
        print("the copied list : ",c)
    elif ch == 10:
        del a;
    else:
        print("Invalid choice!!")
