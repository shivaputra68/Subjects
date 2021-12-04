def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var2 in vartuple:
        print (var2, vartuple)
    return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
printinfo( 70, 60, 50, 40, 30, 20, 10, -1 )

