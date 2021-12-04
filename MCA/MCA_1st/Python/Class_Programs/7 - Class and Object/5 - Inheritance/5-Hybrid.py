class Base1:

    def Display(self):
        print ("Printing from Base class 1")


class Base2:

    def Display(self):
        print ("Printing from Base class 2")


class Derived(Base1, Base2):
    pass



class Hybrid(Derived):
    pass



D = Hybrid()
D.Display()
Base1.Display(D)
Base2.Display(D)
