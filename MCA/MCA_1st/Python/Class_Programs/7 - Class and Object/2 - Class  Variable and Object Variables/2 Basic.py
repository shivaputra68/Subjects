class Employee:
    amount = 1.04
    
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@gmail.com"

    def fullname(self):
        return self.first + " "+ self.last
   
    def raise_amount(self):
        self.pay = int(self.pay * Employee.amount)
        

e1 = Employee("Teju","Kumar",50000)
e2 = Employee("Raju","Maheswari",60000)

print(e1.pay)
print(e2.pay)
e1.raise_amount()
e2.raise_amount()
print(e1.pay)
print(e2.pay)
Employee.amount = 1.05
e1.raise_amount()
e2.raise_amount()
print(e1.pay)
print(e2.pay)
e1.amount = 1.09
e1.raise_amount()
e2.raise_amount()
print(e1.pay)
print(e2.pay)
