while 1:
    try:
        n1 = int(input("Enter the integer number1 --> "))
        n2 = int(input("Enter the integer number2 --> "))
        c = n1 / n2
        print ("Division of two number==> ",c)
        print ("-"*60)
        print (d)
    except ZeroDivisionError:
        print ("ZeroDivisionError Plz enter the correct input ")
    except ValueError:
        print ("ValueError Plz enter the correct input ")
    except NameError:
        print ("NameError Plz enter the correct input ")








