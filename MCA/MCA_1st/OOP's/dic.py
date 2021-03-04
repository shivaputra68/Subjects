#dictionary operations
d={}
class Employee:

    def salary(self,name,address,pan,basic,tds=0,deduct=0):
        self.name=name
        self.address=address
        self.pan=pan
        self.basic=basic
        self.tds=tds
        self.deduct=deduct
        self.hra=basic*1.175
        self.da=0.25*basic
        self.pf=2000
        self.pa=1000
        net_sal=self.basic+self.da+self.hra-(self.pf+self.pa+self.deduct)
        return net_sal

    def __init__(self):
        name=input("Enter the Employee name : ")
        address=input("Enter the Employee address : ")
        pan=input("Enter the pan number : ")
        basic=int(input("Enter the basic salary : "))
        tds=int(input("Enter the tax deduct amount : "))
        deduct=int(input("Enter the deduction amount : "))
        self.net_sal=self.salary(name,address,pan,basic,tds,deduct)

    def display(self):
        print("Employee name : ",self.name)
        print("Employee Address : ",self.address)
        print("Employee pan number : ",self.pan)
        print("Employee basic salary : ",self.basic)
        print("deduction amount : ",self.deduct)
        print("tax deduction of source : ",self.tds)
        print("House rent allowance : ",self.hra)
        print("Dearness allowance : ",self.da)
        print("total salary : ",self.net_sal)

    def search(self,name):
        for k,v in d.items():
            print("k = ",k)
            print("V = ",v)
            if v == name:
                print(v.display())

while True:
    print("1 : Enter Employee details ")
    print("2 : display Employee details")
    print("3 : update to dictionay")
    print("4 : search Employee details")
    print("5 : exit")

    ch=int(input("Enter your choice : "))
    if ch == 1:
        e=Employee()
    elif ch == 2:
        e.display()
    elif ch == 3:
        d.update({e.name:e})
        print(d)
    elif ch == 4:
        s=input("Enter the employee name : ")
        e.search(s)
    elif ch == 5:
        break
