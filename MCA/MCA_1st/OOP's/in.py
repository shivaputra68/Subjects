class base1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class base2:
    def display(self):
        print(self.name)
        print(self.age)

class child(base1,base2):
    def email(self):
        email1=self.name + "@rvce.edu.in"
        print(email1)
c=child("shiva",21)
c.display()
c.email()
