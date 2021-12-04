class Employee:
    raise_amount = 1.04
    count = 0
    
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@gmail.com"

    def fullname(self):
        return self.first + " "+ self.last

    def raise_salary(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

e1 = Developer("Teju","Kumar",50000)
e2 = Employee("Raju","Maheswari",60000)


print (e1.pay)
e1.raise_salary()
print (e1.pay)

"""print (e1.pay)
print (e2.pay)

e1.raise_amount = 1.05
print (Employee.raise_amount)
print (e1.raise_amount)
print (e2.raise_amount)

e1.raise_salary() """
