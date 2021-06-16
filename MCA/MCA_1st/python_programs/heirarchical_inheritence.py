#Heirarchical inheritance
class Student:
    def __init__(self,usn=None,name=None,age=None):
        self.usn = usn
        self.name = name
        self.age = age

    def getdata(self):
        self.usn = input("Enter USN : ")
        self.name = input("Enter Name : ")
        self.age = int(input("Enter age : "))

    def display(self):
        print("student USN : ",self.usn)
        print("student name : ",self.name)
        print("student age : ",self.age)

class PGStudent(Student):
    def __init__(self,sem=None,stipend=None,fee=None):
        self.sem = sem
        self.stipend = stipend
        self.fee = fee

    def ugdata(self):
        self.sem = input("Enter Semister : ")
        self.stipend = int(input("Enter the Stipend : "))
        self.fee = int(input("Enter the fees : "))

    def display(self):
        super().display()
        print("Semister : ",self.sem)
        print("College Fee : ",self.fee)
        print("Stipend : ",self.stipend)

class UGStudent(Student):
    def __init__(self,sem=None,fee=None,stipend=None):
        self.sem = sem
        self.fee = fee
        self.stipend = stipend

    def ugdata(self):
        self.sem = input("Enter Semister : ")
        self.fee = int(input("Enter fees : "))
        self.stipend = int(input("Enter stipend : "))

    def display(self):
        super().display()
        print("Semister : ",self.sem)
        print("College fees : ",self.fee)
        print("Stipend : ",self.stipend)

u = UGStudent()
p = PGStudent()
while True:
    print("1: Display UG details ")
    print("2: Display PG details ")
    print("3: Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        u.getdata()
        u.ugdata()
        u.display()
    elif ch == 2:
        p.getdata()
        p.pgdata()
        p.display()
    elif ch == 3:
        break;
    else:
        print("Invalid option!")
