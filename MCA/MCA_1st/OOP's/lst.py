#List operations 
A=[]
B=[]
n=int(input("Enter the size of list 1 "))
m=int(input("enter the size of list 2 "))
for i in range(0,n):
    a=int(input("enter the list 1 elements : "))
    A.append(a)
for i in range(0,m):
    b=int(input("enter the list 2 elements : "))
    B.append(b)
print(A)
print(B)
while True:
    print("1 : concatination")
    print("2 : copy")
    print("3 : length")
    print("4 : index")
    print("5 : count")
    print("6 : reverse")
    print("7 : find")
    print("8 : sort")
    print("9 : remove")
    print("10 : insert")
    ch=int(input("Enterr your choice : "))
    if ch == 1:
        print("the concatenation of list ",A," and ",B," is : ",A+B)
    elif ch == 2:
        C=A.copy()
        print("the list ",A," is copied to list : ",C)
    elif ch == 3:
        print("the length of the list ",A," is : ",len(A))
    elif ch == 4:
        a=int(input("Entter the element of list : "))
        print("The index value of ",a," is : ",A.index(a))
    elif ch == 5:
        a=int(input("Enter the element to be count : "))
        print("The element ",a," is occured : ",A.count(a))
    elif ch == 6:
        print("The list elements before reversing : ",A)
        A.reverse()
        print("the elements after reversing : ",A)
    elif ch == 7:
        a=int(input("Enter the element to be find : "))
        print("the element",a," is in ",A," ? : ",a in A)
    elif ch == 8:
        print("before sorting the list elements : ",A)
        A.reverse()
        print("after sorting the list elements : ",A)
    elif ch == 9:
        a=int(input("Enter the element to be removed "))
        A.remove(a)
        print("the list after removing ",a," is : ",A)
    elif ch == 10:
        a=int(input("Enter the list element to be inserted : "))
        b=int(input("Enter the position of the list"))
        A.insert(b,a)
        print("the list after inserting ",a," is ",A)
    else:
        print("Invalid choice")
