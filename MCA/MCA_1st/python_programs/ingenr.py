import time

def timeit(func):
    def timed(*args, **kw):
        print("Before the Timeit decorator")
        #start time
        ts = time.time()
        #function returned result
        result = func(*args, **kw)
        #function end time
        te = time.time()


        #calculating the function time taken
        minutes, seconds = divmod((te-ts), 60)
        print(minutes,seconds)
        print ("time taken %8.2f * 10 exp 6"%((te-ts)*10**6))
        print("After the Timeit decorator")
        return result
    return timed


@timeit
#Generator for the fibonacci series
def fib():
    a,b=0,1
    while(1):
        yield a
        a, b=b ,a+b


#Main Function Starts for the calling program
#accept number of fibonacci series to be generated
num = int(input("enter the size for fibonacci series"))

#assign fib definition for the variable
fibonacci = fib()

#iterate in the for loop to yield next numbers
for x in range(num):
    #generator the next number in the series
    print(next(fibonacci))  
