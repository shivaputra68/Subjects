try:
    n1 = int(input("Enter the integer number1 --> "))
    n2 = int(input("Enter the integer number2 --> "))
    c = n1 / n2
    print ("Division of two number==> ",c)
    print(d)
except (ZeroDivisionError, NameError):
    print ("Division of two number with Zero not possible")


print ("Try Again")




