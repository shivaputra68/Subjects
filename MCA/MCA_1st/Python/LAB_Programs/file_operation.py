#File concept and exception handling
while True:
    print("1: Enter the source and destination file names to open")
    print("2: Opening a file in read and write mode")
    print("3: Wirte a file ")
    print("4: read a file ")
    print("5: Copy file")
    print("6: close file ")
    c = int(input("Enter your choice : "))
    if c == 1:
        sname = input("Enter Source file name : ")
        dname = input("Enter Destination file name : ")
    elif c == 2:
        try:
            f=open(sname,'r')
            e=open(dname,'w')
            print("Files opened successfully")
        except FileNotFoundError:
            print("File not foud error")
        except NameError:
            print("invalid name error")
        except KeyboardInterrupt:
            print("Wrong key pressed")
    elif c == 3:
        try:
            a = f.read()
            e.write(a)
            print("Successfully copied")
            f.close()
            e.close()
        except NameError:
            print("Name error")
    elif c == 4:
        try:
            e.read()
        except ValueError:
            print("please open the file ")
        except NameError:
            print("name is not defined")
    elif c == 5:
        try:
            f=open(sname,'r')
            e=open(dname,'w')
            a=f.read()
            e.write(a)
            print("file copied successfully")
            f.close()
            e.close()
        except IOError:
            print("cant open file or read data")
        except NameError:
            print("Namer error")
    elif c == 6:
        try:
            print(f/e)
        except TypeError:
            print("Invalid operations")
        except NameError:
            print("Name Error")
