# Basic Program for Inheritance
class Employee:
    raise_amt = 1.04
    
    def __init__(self,first,last,empid,pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay
    def fullname(self):
        return self.first + self.last
        
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,empid,pay,pgl):
        super().__init__(first,last,empid,pay)
        #Employee.__init__(self,first,last,empid,pay)
        self.pgl =pgl
        

emp1 = Developer("Ravi", "Shankar", 1001, 50000, "Python")
emp2 = Developer("Shashi", "Kumar", 1002, 60000,"Java")

#print(help(Developer))
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print (emp1.pgl)

