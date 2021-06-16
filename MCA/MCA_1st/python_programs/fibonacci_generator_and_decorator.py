#ibonacci series exexution using generator and decorator
import time
def timeit(func):
    def timed(*args,**kw):
        print("Before the timeit decorator ")
        ts=time.time()
        result=func(*args,**kw)
        te=time.time()

        minutes,seconds = divmod((te-ts),60)
        print(minutes,seconds)
        print("time taken %8.2f * 10 exp 6"%((te-ts)*10**6))
        print("After the  timeit decorator")
        return result
    return timed

@timeit
def fib():
    a,b=0,1
    while(1):
        yield(a)
        a,b=b,a+b

n=int(input("Enter the size : "))
fibonacci = fib()
for i in range(n):
    print(next(fibonacci))
