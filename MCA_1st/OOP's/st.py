#sting operations
s1=input("Enter the string 1 : ")
s2=input("Enter the string 2 : ")
while True:
    print("1:concatination")
    print("2:count")
    print("3:uppercase")
    print("4:lowercase")
    print("5:slice")
    print("6:replace")
    print("7:length")
    print("8:index value")
    print("9:isnumeric")
    print("10:title string")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        print("The concatination of ",s1," and ",s2," is : ",s1+s2)
    elif ch == 2:
        c=input("Enter the character to be count : ")
        print("The character ",c," is in the string ",s1," is there : ",s1.count(c))
    elif ch == 3:
        print("the uppercase of ",s1," is : ",s1.upper()," and ",s2,"is : ",s2.upper())
    elif ch == 4:
        print("the lowercase of ",s1," is : ",s1.lower()," and ",s2,"is : ",s2.lower())
    elif ch == 5:
        a=int(input("Enter the starting index value : "))
        b=int(input("Enter the end index value : "))
        print("the characters from ",a," to ",b," are : ",s1[a:b])
    elif ch == 6:
        c=input("Enter the character to be removed : ")
        n=(input("Enter the character to be replaced : "))
        print("the character ",c," is replaced with ",n," then : ",s1.replace(c,n))
    elif ch == 7:
        print("the length of ",s1," is : ",len(s1)," and ",s2," is : ",len(s2))
    elif ch == 8:
        c=input("Enter the character : ")
        print("the index value of ",c," is ",s1.index(c))
    elif ch == 9:
        print("the string ",s1," is numeric : ",s1.isnumeric())
    elif ch == 10:
        print("the string ",s2," title form is ",s1.title())
    else:
        print("Invalid syntax")
