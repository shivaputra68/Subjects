class Father:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def name(self):
        print ("Father: ", self.first, self.last)

    def Age(self):
        print ("Age == ",self.age)

class Son(Father):
    def name(self):
        print("Son ", self.first, self.last)

class Daughter(Father):
    def name(self):
        print("Daughter ", self.first, self.last)
F = Father("Jon", "Cena", 45)
S = Son("sam","Sample", 15)
D = Daughter("Riya","Tej",10)
F.name()
S.name()
D.name()
F.age()
S.age()
D.age()
