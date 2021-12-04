class Student:
    def __init__(self,usn = None, name = None, age = None):
        self.name = name
        self.usn = usn
        self.age = age

    def get_elments(self):
        self.name = input("Enter the name of Student ")
        self.usn = input("Enter the USN of Student ")
        self.age = input("Enter the age of Student ")

class Subject(Student):
    def __init__(self,sem = 0, sub1 = 0, sub2 = 0, sub3 = 0, sub4 = 0,sub5 = 0):
        self.sem = sem
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5

    def get_Marks(self):
        self.sem = input("Enter the Semester ")
        print("Plz enter the Marks for respective subjects")
        self.subject1 = input("Enter the Subject 1")
        self.sub1 = int(input("Enter the marks for %s"%(self.subject1)))
        self.subject2 = input("Enter the Subject 2")
        self.sub2 = int(input("Enter the marks for sub2 %s"%(self.subject2)))
        self.subject3 = input("Enter the Subject 3")
        self.sub3 = int(input("Enter the marks for sub3 %s"%(self.subject3)))
        self.subject4 = input("Enter the Subject 4")
        self.sub4 = int(input("Enter the marks for sub4 %s"%(self.subject4)))
        self.subject5 = input("Enter the Subject 5")
        self.sub5 = int(input("Enter the marks for sub5 %s"%(self.subject5)))

class Results(Subject):
    def display(self):
        print(self.name)
        print(self.usn)
        print(self.age)
        self.total = self.sub1+ self.sub2 +self.sub3 +self.sub4 +self.sub5
        print("total Marks == ", self.total)
        self.percentage = ((self.total /500)*100)
        print(self.percentage)


s1 = Results()
s1.get_elments()
s1.get_Marks()
s1.display()

