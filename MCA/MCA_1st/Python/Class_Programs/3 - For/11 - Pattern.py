num = int(input("Enter the  number of Rows "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end='')
    for a in range(num+1-i,0,-1):
        print(a,end="")
        
    print()
