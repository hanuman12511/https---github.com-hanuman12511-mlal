
import os
class Exists:
    def ExistFile(self,filename):
        
        if(os.path.exists(filename)):
            return True
        return False
class RemoveFile:
    print("")
class GetDir:
    print("")
class AddDir:
    print("")
class WriteData:
    def __init__(self):
        #file = open("filename","mode w,r,a")
        filename  = input("enter file name")
        obj = Exists()
        ex= obj.ExistFile(filename)
       
        if(ex):
           print("file exist")

        else:
            file = open(filename,"w")
            data = input("enter information")
            file.write(data)
            file.close()
            
class ReadData:
        def __init__(self):
            filename  = input("enter file name")
            obj = Exists()
            ex= obj.ExistFile(filename)
            if(ex):
                file= open(filename,"r")
                for data in file:
                    print(data)
            else:
                print("file not found")
class AppendData:
    print("")



while(True):
    ch = int(input("enter 1for create new file\nenter 2 for read\nenter 3 for append data "))
    if(ch == 1):
        obj = WriteData()
    elif(ch ==2):
        obj=ReadData()
        