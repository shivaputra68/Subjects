#2. Multilevel Inheritance
class Animal:  #Grandfather 
    def eat(self):  
      print ('Eating...')

class Dog(Animal): # Father
    def bark(self):
        print ('Dog is Barking...')

class BabyDog(Dog):  #Child
    def weep(self):  
        print ('Weeping...')

    def bark(self):
        print ("Baby Dog is Barking")
d=BabyDog()
help(BabyDog)
d.eat()  
d.bark()  
d.weep() 
