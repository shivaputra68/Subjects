class Employee:
    amount = 1.04
    count = 0
    
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@gmail.com"
        Employee.count =  Employee.count + 1

    def fullname(self):
        return self.first + " "+ self.last
   
    def raise_amount(self):
        self.pay = int(self.pay * Employee.amount)
        return self.pay

    @classmethod
    def assign_amount(cls,a):
        cls.amount = a

        
print(Employee.amount)
emp1 = Employee("Teju","Kumar",50000)
emp2 = Employee("Raju","Maheswari",60000)
print(Employee.amount)

print(Employee.amount)
print(emp1.amount)
print(emp2.amount)
Employee.amount = 1.05
print(Employee.amount)
print(emp1.amount)
print(emp2.amount)
Employee.assign_amount(100)
print(Employee.amount)
emp1.amount = 1.09
print(emp1.amount)
print(emp2.amount)

