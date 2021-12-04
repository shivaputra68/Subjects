sname=input("Enter Existing file name ")
dname=input("Enter new file name ")
try:
   A=open(sname, "r") 
   B = open(dname, "w")
   str1=A.read() 
   B.write(str1)
except IOError:
   print ("Error: can\'t find file or read data ")
else:
   print ("File successfully copied ")
   A.close()
   B.close()
