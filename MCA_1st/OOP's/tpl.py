#tuple operation
global A
global B
n=int(input("enter the size of tuple 1 : "))
a=[];b=[]
for i in range(0,n):
    b=int(input("Enter the element : "))
    a.append(b)
A=tuple(a)
m=int(input("enter the size of tuple 2 : "))
b=[]
for i in range(0,m):
    c=int(input("Enter the element : "))
    b.append(c)
B=tuple(b)
print("A = ",A)
print("B = ",B)
while 1:
    print("1 : addition")
    print("2 : repetation")
    print("3 : maximum ")
    print("4 : minimum")
    print("5 : length")
    print("6 : range slicing ")
    print("7 : slicing")
    print("8 : index")
    print("9 : count")
    print("10 : delete element")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        print("the concatenation of tuple ",A," and tuple ",B," is : ",A+B)
    elif ch == 2:
        print("the repetation of tuple ",A," is : ",A*2)
    elif ch == 3:
        print("The maximum vlaue of tuple ",A," is ",max(A))
        print("The maximum value of tuple ",B," is ",max(B))
    elif ch == 4:
        print("The minimum vlaue of tuple ",A," is ",min(A))
        print("The minimum value of tuple ",B," is ",min(B))
    elif ch == 5:
        print("The length of tuple ",A," is ",len(A))
        print("the length of tuple ",B," is ",len(B))
    elif ch == 6:
        a=int(input("enter the starting index : "))
        b=int(input("enter the ending index : "))
        print("the range slicing from ",a," to ",b," is ",A[a:b])
    elif ch == 7:
        a=int(input("enter the index number : "))
        print("the sliced tuple is : ",A[a:])
    elif ch == 8:
        a=int(input("enter the element : "))
        print("the index value of ",a," is : ",A.index(a))
    elif ch == 9:
        a=int(input("enter the element : "))
        print("the number of ",a," are : ",A.count(a))
    elif ch == 10:
        del A
        print("after tuple is deleted")
    else:
        print("Invalid syntax")
