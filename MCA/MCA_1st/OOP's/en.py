class encp:
    def __init__(self,a,b,c):
        self.atta=a
        self.__attb=b
        self._attc=c
    def __disp(self):
        print("private data ",self.__attb)
        print("noraml data ",self.atta)
    def display(self):
        self.__disp()
    def _prt(self):
        print(self._attc)

class encp1(encp):
    def call(self):
        self._prt()

a=encp1(10,20,30)
a.display()
a.call()
