#multilevel inheritance
class Student:
    def __init__(self,name=None,usn=None,branch=None):
        self.name = name
        self.usn = usn
        self.branch = branch

    def getdata(self):
        self.name = input("Enter name : ")
        self.usn = input("Enter usn : ")
        self.branch = input("Enter Branch : ")

    def display(self):
        print("***************************************")
        print("Student Name : ",self.name)
        print("Student usn : ",self.usn)
        print("Branch Name : ",self.name)

class Marks(Student):
    def __init__(self,s1=None,s2=None,s3=None,s4=None,s5=None):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

    def getmarks(self):
        self.s1 = int(input("Enter subject 1 marks : "))
        self.s2 = int(input("Enter subject 2 marks : "))
        self.s3 = int(input("Enter subject 3 marks : "))
        self.s4 = int(input("Enter subject 4 marks : "))
        self.s5 = int(input("Enter subject 5 marks : "))

    def display(self):
        super().display()
        print("***************************************")
        print("Subject 1 marks ",self.s1)
        print("Subject 2 marks ",self.s2)
        print("Subject 3 marks ",self.s3)
        print("Subject 4 marks ",self.s4)
        print("Subject 5 marks ",self.s5)


class Result(Marks):
    def calculate(self):
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5
        self.per = (self.total * 100) / 500

    def display(self):
        super().display()
        print("***************************************")
        print("Total Marks : ",self.total)
        print("Percentage : ",self.per)
        print("***************************************")

r = Result()
r.getdata()
r.getmarks()
r.calculate()
r.display()
