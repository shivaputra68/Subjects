def hi(n):
    print ("The value of n == %d",n)
    if n==0:
        return
    else:
        hi(n-1)

hi(10)
