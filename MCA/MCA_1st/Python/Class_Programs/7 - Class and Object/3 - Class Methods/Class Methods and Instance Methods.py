class Employee:
    amount = 1.04
    count = 0

    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay                       
        self.email = first+last+"@company.com"
        Employee.count = Employee.count+1
        

    def fullname(self):                   #Regular or Instance Method
        return self.first+" "+self.last
    def Hello(self):
        return self.fullname()

    def raise_amount(self):                 #Regular or Instance Method
       self.pay =  int(self.pay * self.amount)
       return self.pay

    @classmethod                            #Class Method
    def set_raise(cls, a):
        cls.amount = a

    @staticmethod                           #Static Method
    def Hi():
        print ("Hello")
    


print("Total Object Created ", Employee.count)        
       
emp1 = Employee("Ashok1","Kumar",50000)
emp2 = Employee("Lokesh1","Raj",40000)
emp1 = Employee("Ashok2","Kumar",50000)
emp2 = Employee("Lokesh2","Raj",40000)
emp1 = Employee("Ashok3","Kumar",50000)
emp2 = Employee("Lokesh3","Raj",40000)
emp1 = Employee("Ashok","Kumar",50000)
emp2 = Employee("Lokesh","Raj",40000)

print("Total Object Created ", Employee.count)

print (Employee.amount)
print(emp1.amount)
print(emp2.amount)
Employee.amount = 1.05
print (Employee.amount)
print(emp1.amount)
print(emp2.amount)
emp1.amount = 1.06
print (Employee.amount)
print(emp1.amount)
print(emp2.amount)
print("-"*60)
Employee.set_raise(100)
print (Employee.amount)
print(emp1.amount)
print(emp2.amount)
Employee.set_raise(200)


