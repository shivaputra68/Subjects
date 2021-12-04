# Function definition is here
def printme( str1 ):
    "This prints a passed string into this function"
    print (str1)
    a = str1
    print(id(a))
    return a

# Now you can call printme function
str2 = printme(5)
print (str2)
print(id(str2))
