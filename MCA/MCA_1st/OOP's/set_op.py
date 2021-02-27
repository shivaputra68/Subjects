#Set operations
A=set()
B=set()
n=int(input("Enter the size of set 1 : "))
for i in range(0,n):
    a=int(input("Enter the set element : "))
    A.add(a)
m=int(input("Enter the size of set 2 : "))
for i in range(0,m):
    b=int(input("Enter the  set element : "))
    B.add(b)
print(A)
print(B)
while True:
    print("1 : check disjoint")
    print("2 : check superset ")
    print("3 : copy")
    print("4 : is membership")
    print("5 : length")
    print("6 : pop")
    print("7 : union")
    print("8 : intersection")
    print("9 : difference")
    print("10 : symmetric difference")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        print("The concatenation of set ",A," and set ",B," is : ",A.isdisjoint(B))
    elif ch == 2:
        a=int(input("Enter the element : "))
        print("The set ",A," is a superset of set ",B," is : ",A.issuperset(B))
    elif ch == 3:
        C=set()
        print("Before copying the set ",C)
        C=A.copy()
        print("The set ",A," is copied then set : ",C)
    elif ch == 4:
        a=int(input("Enter the element to be check : "))
        print("The element ",a," is in the set : ",A," ? ",a in A)
    elif ch == 5:
        print("the length of set ",A," is : ",len(A))
        print("the length of set ",B," is : ",len(B))
    elif ch == 6:
        print("Before poping the set element : ",A)
        A.pop()
        print("After poping the set  ",A," element  the set : ",A," is : ",A)
    elif ch == 7:
        print("The union of set ",A," and set ",B," is : ",A.union(B))
    elif ch == 8:
        print("The intersection of set ",A," and set ",B," is : ",A.intersection(B))
    elif ch == 9:
        print("The difference between set ",A," and set ",B," is : ",A.difference(B))
    elif ch == 10:
        print("The symetric function of set ",A," and set ",B," is : ",A.symmetric_difference(B))
    else:
        print("Invalid entry")
