class Employee:
    raise_amount = 1.04  # Class Variable
    count = 0            # Class Variable
    
    def __init__(self, first,last,pay):
        self.first = first                      # Instance Variable
        self.last = last                        # Instance Variable
        self.pay = pay                          # Instance Variable
        self.email = first+last+"@gmail.com"    # Instance Variable

    def fullname(self):
        return self.first + " "+ self.last

    def raise_salary(self):
        self.pay = int(self.pay * self.raise_amount)


e1 = Employee("Teju","Kumar",50000)
e2 = Employee("Raju","Maheswari",60000)

print (e1.pay)
print (e2.pay)

e1.raise_amount = 1.05
print (Employee.raise_amount)
print (e1.raise_amount)
print (e2.raise_amount)

e1.raise_salary()
