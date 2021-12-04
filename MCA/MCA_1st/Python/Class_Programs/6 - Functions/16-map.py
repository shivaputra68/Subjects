# Map : The map(aFunction, aSequence) function applies a passed-in
# function to each item in an iterable object and returns a list containing
# all the function call results.



"""items = [1, 2, 3, 4, 5]
squared = []
for x in items:
    squared.append(x ** 2)

print (squared)"""



items = [1, 2, 3, 4, 5]
def sqr(x): return x ** 2

print(list(map(sqr, items)))

