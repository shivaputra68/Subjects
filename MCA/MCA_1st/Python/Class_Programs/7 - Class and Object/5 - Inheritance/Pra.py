# Multiple

class base1:
    def Hello(self):
        print ("Message from Base class 1 ")

class base2:
    def Hello(self):
        print ("Message from Base class 2 ")

class Derived(base2,base1):
    pass


d = Derived()
#d.Hello()
base1.Hello(d)

base2.Hello(d)
