#overloading concept
class Person:
    def hello(self,name=None,age=None):
        self.name = name
        self.age = age
        if self.name != None and self.age != None:
            print("Hello My name : ",self.name," and Age : ",self.age)
        elif self.name != None:
            print("Hello My name : ",self.name)
        elif self.age != None:
            print("Hello My age : ",self.age)
        else:
            print("hello")

p = Person()
print("method call with no argument")
p.hello()
print("Method call  with 1st arguemnt ")
p.hello(name = "shiva")
print("Method call with 2nd argument")
p.hello(age = 21)
print("Method call with two argument")
p.hello(name = "shiva", age = 21)
