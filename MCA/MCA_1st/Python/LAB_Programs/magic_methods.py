#User defined modules using magic method
class Operation:
    def __init__(self):
        self.alist = []
        n = int(input("Enter size of a list"))
        for i in range(0,n):
            self.alist.append(int(input("Enter value : ")))
        print(self.alist)

    def __add__(num1,num2):
        nlist = []
        for i in range(0,len(num1.alist)):
            nlist.append(num1.alist[i] + num2.alist[i])
        return nlist

    def __sub__(num1,num2):
        nlist = []
        for i in range(0,len(num1.alist)):
            nlist.append(num1.alist[i] - num2.alist[i])
        return nlist

    def __mul__(num1,num2):
        nlist = []
        for i in range(0,len(num1.alist)):
            nlist.append(num1.alist[i] * num2.alist[i])
        return nlist

    def __div__(num1,num2):
        nlist = []
        for i in range(0,len(num1.alist)):
            nlist.append(num1.alist[i] / num2.alist[i])
        return nlist

    def __floordiv__(num1,num2):
        nlist = []
        for i in range(0,len(num1.alist)):
            nlist.append(num1.alist[i] // num2.alist[i])
        return nlist
