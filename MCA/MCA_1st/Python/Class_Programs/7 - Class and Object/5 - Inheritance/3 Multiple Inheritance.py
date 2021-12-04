# 3. Multiple Inheritance

class base1:
    def hello(self):
        print ("Message from Base class 1")

class base2:
    def hello(self):
        print ("Message from Base class 2")

class Derived(base1, base2):
    pass

d1 = Derived()

d1.hello()
base2.hello(Derived)

"""
base1.hello(Derived)
print("-"*60)
base2.hello(Derived)
print("-"*60)
d1.hello() """

