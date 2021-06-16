#method overriding
class Employee:
    raise_amount = 1.10

    def __init__(self,name,age,pay):
        self.name = name
        self.age = age
        self.pay = pay

    def salary(self):
        self.pay = self.raise_amount * self.pay
        print("Employee Raised salary : ",self.pay)

    def display(self):
        print("Employee Name : ",self.name)
        print("Employee Age : ",self.age)
        print("Before raise the payment : ",self.pay)

class Developer(Employee):
    raise_amount = 1.06

    def salary(self):
        self.pay = self.pay * self.raise_amount
        print("Developer Raised salary : ",self.pay)

d = Developer("shiva",21,40000)
e = Employee("Amar",21,40000)
e.display()
e.salary()

d.display()
d.salary()
