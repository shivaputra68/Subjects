class Student:
    def __init__(self, name= " " ,usn = " " ,age= " "):
        self.name = name
        self.usn = usn
        self.age = age

    def get_element(self):
        self.name = input("Enter The Name ")
        self.usn = input("Enter The USn ")
        self.age = input("Enter The Age ")

    def display(self):
        print (self.name)
        print (self.usn)
        print (self.age)
        

class UG_Student(Student):
    def __init__(self, sem = 0, fees = 0, stipend= 0):
        self.sem = sem
        self.fees = fees
        self.stipend = stipend

    def get_UGelement(self):
        self.sem = input("Enter The sem ")
        self.fees = input("Enter The fees ")
        self.stipend = input("Enter The Stipend ")


    def UGdisplay(self):
        print (self.sem)
        print (self.fees)
        print (self.stipend)

class PG_Student(Student):
    def __init__(self, sem = 0, fees = 0, stipend= 0):
        self.sem = sem
        self.fees = fees
        self.stipend = stipend

    def get_PGelement(self):
        self.sem = input("Enter The sem ")
        self.fees = input("Enter The fees ")
        self.stipend = input("Enter The Stipend ")


    def PGdisplay(self):
        print (self.sem)
        print (self.fees)
        print (self.stipend)
        
        
s = UG_Student()
s.get_element()
s.get_UGelement()
s.display()
s.UGdisplay()

s = PG_Student()
s.get_element()
s.get_PGelement()
s.display()
s.PGdisplay()
