#dictionary operations
d={}
class Employee:
    def salary(self,name,address,pan,basic,hra,da,pf,pa,tds=0,deduct=0):
        self.name = name
        self.address = address
        self.pan = pan
        self.basic = basic
        self.hra = hra
        self.da = da
        self.pf = pf
        self.pa = pa
        self.tds = tds
        self.deduct = deduct
        self.net_sal = self.basic + self.hra + self.da - (self.pf + self.pa + self.tds + self.deduct)
        return self.net_sal

    def __init__(self):
        name = input("Enter the name : ")
        address = input("Enter  the address : ")
        pan = input("Enter the Pan number : ")
        basic = int(input("Enter the basic salary : "))
        hra = int(input("Enter the house rent allowence : "))
        da = int(input("Enter the drink allowence : "))
        pf = int(input("Enter the pf amount : "))
        pa = int(input("Enter the pa amount : "))
        tds = int(input("Enter tds : "))
        deduct = int(input("Enter deduct : "))
        net_sal = self.salary(name,address,pan,basic,hra,da,pf,pa,tds,deduct)

    def display(self):
        print("Name : ",self.name)
        print("Address : ",self.address)
        print("pan no : ",self.pan)
        print("Basic salary : ",self.basic)
        print("hra : ",self.hra)
        print("da : ",self.da)
        print("pf : ",self.pa)
        print("pa : ",self.pa)
        print("tds : ",self.tds)
        print("deduct : ",self.deduct)
        print("Total salary : ",self.net_sal)

    def search(self,name):
        for k,v in d.items():
            print("K = ",k)
            print("V = ",v)
            if k == name:
                print(v.__dict__)

while 1:
    print("1: Enter the Employee details ")
    print("2: display the employee details ")
    print("3: update the dictionary ")
    print("4: search the employee ")
    print("5: exit")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        e = Employee()
    elif ch == 2:
        e.display()
    elif ch == 3:
        d.update({e.name : e})
        print("The dictionary updated")
    elif ch == 4:
        s = input("Enter the employee name : ")
        e.search(s)
    elif ch == 5:
        break;
    else :
        print("Invalid choice!!")
