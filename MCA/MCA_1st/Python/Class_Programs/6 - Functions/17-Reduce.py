# Reduce function
from functools import reduce

a = [2,3,5,7,11,13,17,19,23,29]
product  = 1
for x in a:
    print (product, x)
    product = product *x
print (product)
    



def multi(c,d):
    return c*d

print(reduce(multi,a))

