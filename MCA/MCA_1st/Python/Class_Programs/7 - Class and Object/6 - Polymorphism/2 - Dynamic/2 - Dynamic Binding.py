#dynamic Binding

class Animal:
    def walk(self):
        print ("Animal is walking")

class Dog(Animal):
    def walk(self):
        print ("Dog is Walking")


D1 = Dog()
D1.walk()
