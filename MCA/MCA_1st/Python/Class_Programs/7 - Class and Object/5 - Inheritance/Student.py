class Student:
    def __init__(self,usn = " ",name=" ",age=0):
        self.usn =usn
        self.name = name
        self.age=age
    def get_element(self):
        self.usn=input("Enter the USN ")
        self.name=input("Enter the Name ")
        self.age=input("Enter the age ")

    def display(self):
        print (self.usn)
        print (self.name)
        print (self.age)

class PG_Student(Student):
    def __init__(self,sem = " ", fees = 0, stipend = 0):
        self.sem = sem
        self.fees = fees
        self.stipend = stipend

    def get_PGelement(self):
        self.sem=input("Enter the sem ")
        self.fees=input("Enter the fees ")
        self.stipend=input("Enter the stipend ")

    def display_PG(self):
        print (self.sem)
        print (self.fees)
        print (self.stipend)


s = PG_Student()
s.get_element()
s.display()
s.get_PGelement()
s.display_PG()

