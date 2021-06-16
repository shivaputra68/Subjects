#String operations
s1 = input("Enter the String1 : ")
s2 = input("Enter the String2 : ")
while 1:
    print("1: Concatinating Strings")
    print("2: UpperCase and LowerCase")
    print("3: Slice")
    print("4: count characters")
    print("5: Replace character")
    print("6: Title format")
    print("7: check character")
    print("8: find length")
    print("9: find index")
    print("10: Delete String")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("The ",s1," + ",s2," : ",s1+s2)
    elif ch == 2:
        print("The upeer case : ",s1.upper())
        print("The lower case : ",s2.lower())
    elif ch == 3:
        n = int(input("Enter the Starting index : "))
        m = int(input("Enter the Ending index : "))
        s=s1[n:m]
        print("The substring : ",s)
    elif ch == 4:
        c = input("Enter the character : ")
        print("The no characters in ",s1," are : ",s1.count(c))
        print("The no characters in ",s2," are : ",s2.count(c))
    elif ch == 5:
        c1 = input("Enter the character to be removed : ")
        c = input("Enter the character to be replaced : ")
        print("The String ",s1," after replacing char ",c," is : ",s1.replace(c1,c))
    elif ch == 6:
        print("The title format of the ",s1," : ",s1.title())
        print("The title format of the ",s2," : ",s2.title())
    elif ch == 7:
        c = input("Enter the character to be check : ")
        print("The character ",c," in ",s1," is there : ",s1.__contains__(c))
    elif ch == 8:
        print("String ",s1," length ",len(s1))
    elif ch == 9:
        c = input("Enter the character : ")
        print("The character ",c," at ",s1.find(c))
    elif ch == 10:
        del(s1);
    else:
        print("Enter valid choice!!")
