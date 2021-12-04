class Employee:
    _amount = 1.04                             # Protected Class Variable
    count = 0
    
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self._pay = pay                        # Protected Instance Variable
        self.email = first+last+"@company.com"
        Employee.count = Employee.count + 1

    def fullname(self):
        return self.first+" "+self.last

    def raise_amount(self):
       self._pay =  int(self._pay * self._amount)
       return self._pay

print(Employee.count)       
emp1 = Employee("Teju","Kumari",50000)
emp2 = Employee("Raju","Kumar",40000)


print(emp1.raise_amount())
print (emp1._amount)




