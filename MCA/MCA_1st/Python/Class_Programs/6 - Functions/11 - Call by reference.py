def my(b):
    print (b)
    b.append("RVCE")
    print (a)
    print (id(a), id(b))

a = [1,2,3,4]
my(a)

print (a)
