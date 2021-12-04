class MCA(Exception):
    def __init__(self,message):
        self.message =message

a = 0
try:
    if a ==1:
        raise MCA("Hello Bangalore")
except MCA as e:
    print(e.message)
