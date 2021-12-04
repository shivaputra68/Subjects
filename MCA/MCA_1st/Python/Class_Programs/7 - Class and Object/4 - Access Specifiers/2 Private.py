class Employee:
    __amount = 1.04                             # Private Class Variable
    count = 0
    
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.__pay = pay                        # Private Instance Variable
        self.email = first+last+"@company.com"
        Employee.count = Employee.count + 1

    def fullname(self):
        return self.first+" "+self.last

    def raise_amount(self):
       self.__pay =  int(self.__pay * self.__amount)
       return self.__pay

print(Employee.count)       
emp1 = Employee("TejU","Kumari",50000)
emp2 = Employee("Raju","Kumar",40000)
print(Employee.count) 

print(emp1.raise_amount())
#print (emp1.__pay)




