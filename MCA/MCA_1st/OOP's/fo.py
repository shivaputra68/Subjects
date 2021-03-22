#function overloading
class Overload:
    def hello(self,name=None,age=None):
        self.name=name
        self.age=age
        if self.name != None and self.age != None:
            print("2 arg Name : ",self.name)
            print("2 arg Age : ",self.age)
        elif self.name != None:
            print("1 arg Name ",self.name)
        else:
            print("Default arg")
c=Overload()
c.hello()
c.hello("shiva")
c.hello("shiva",21)
