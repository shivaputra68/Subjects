#1. Inheritance in Python example
class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,empid,pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay
        
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amt)

        
class Developer(Employee):
    pass


class Manager(Employee):
    pass

emp1 = Manager("Ravi", "Shankar", 1001, 50000)
emp2 = Developer("Shashi", "Kumar", 1002, 60000)


