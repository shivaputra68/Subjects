class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+"@gmail.com"

    def fullname(self):
        return self.first + " "+ self.last
      

e1 = Employee("Raju","Kumar", 50000)
e2 = Employee("Teju", "Kumari",60000)
e3 = Employee("Teju3", "Kumari3",60001)
e4 = Employee("Teju4", "Kumari4",60002)
e5 = Employee("Teju5", "Kumari5",60003)

print (e1.first+e1.last)
print (Employee.fullname(e1))
print (e1.fullname())

print (Employee.fullname(e2))
print (e2.fullname())
