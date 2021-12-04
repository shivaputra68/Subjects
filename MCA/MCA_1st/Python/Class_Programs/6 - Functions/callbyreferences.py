def callbyreference(a):
    print( "The value of a in fuction before appending = ", a)
    a.append("RVCE")



a = [5,10,3.2]
print( "The value of a = ", a)
callbyreference(a)
print( "The value of a = ", a)

