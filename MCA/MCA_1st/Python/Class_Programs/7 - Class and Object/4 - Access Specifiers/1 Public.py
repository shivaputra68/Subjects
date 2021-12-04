class Employee:
    "Hello MCA RVCE 1st Sem Bangalore "
    amount = 1.04                             # All Class Variable are Public
    count = 0
    
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay                       # All Instance Variable are Public 
        self.email = first+last+"@company.com"
        Employee.count = Employee.count + 1

    def fullname(self):
        return self.first+" "+self.last

    def raise_amount(self):
       self.pay =  int(self.pay * self.amount)
       return self.pay

print(Employee.count)       
emp1 = Employee("Teju","Kumari",50000)
emp2 = Employee("Raj","Kuram",40000)


#print(emp1.raise_amount())
print (emp1.amount)




