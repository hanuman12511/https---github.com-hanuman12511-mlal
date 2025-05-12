  

# class Info :
#     name=""
#     emp_id=""

#     def __init__(self,n,eid):
#         self.name =n
#         self.emp_id = eid 
#     def showData(self):
#         print("")


# class Project(Info):
#     project = ""
#     def __init__(self, n, eid,project):

#         super().__init__(n, eid)
#         self.project = project
#     def showData(self):
#         try:
#             print("Project",self.project)
#             print("empid",self.emp_id)
#             print("name",self.name)
#         except:
#             print("Error")

# class Emp (Info) :
#     salary = ""
#     def __init__(self, n, eid,salary):
#         super().__init__(n, eid)
#         self.salary = salary
    
#     def showData(self):
#         print("empid",self.emp_id)
#         print("name",self.name)
#         print("salary",self.salary)


# n = input("enter name")
# eid = input("enter empid")
# salary = input("enter salary")
# obj = Emp(n,eid,salary)
# obj.showdata()

# p = input("enter project name")
# obj = Project(n,eid,p)
# obj.showproject()


  
    #  {}  ,:

# dataset = {}
# emaillist=[]
# passwordlist=[]


# class Home:
#     def __init__(self,email):
#         print("hello !! "+email)
#         input()


# class Register:
#     email=''
#     password=''
#     def __init__(self,e,p):
#         self.email=e
#         self.password=p
#         self.saveData()
#     def saveData(self):
#         emaillist.append(self.email)
#         passwordlist.append(self.password)
#         dataset.update({"email":emaillist,"password":passwordlist})
      


# class Login:
#     email=''
#     password=''
#     def __init__(self,e,p):
#         self.email = e
#         self.password = p
#         self.userLogin()
#     def userLogin(self):
#         for i  in range(len(dataset['email'])):
#             if(self.email == dataset['email'][i]):
#                 break
#         else:
#             print("email not found")
#         if(self.password ==  dataset['password'][i]):
#             home = Home(self.email)

# while(True):
#     ch = int(input("1 for register\n2 for login"))
#     email = input("enter email")
#     password = input("enter passwrod")
#     if(ch == 1):
        
#         register = Register(email,password)
#     elif (ch == 2):
#         Login(email,password)




# class Demo: 
#     name=""
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         return self.name

# name= input("enter name")
# obj =Demo(name)
# print(obj.getData())



# class Demo: 
#     name=""
#     def setData(self,name):
#         self.name=name
#     def getData(self):
#         print(self.name)

# name= input("enter name")
# obj =Demo()
# obj.setData(name)
# obj.getData()
#print(obj)


# class Demo: 
#     name=""
#     def __init__(self):
#         print("*******************")
#         self.name=input("enter name")
#     def __str__ (self):
#         return self.name


# obj =Demo()
# print(obj)

# class Demo: 
#     name=""
#     def __init__(self):
#         print("*******************")
#         self.name=input("enter name")
#     def showdata(self):
#         print(self.name)


# obj =Demo()
# obj.showdata()

        


# def fun():
#     print("hello")


# class Demo: 
#     name = "";
#     def setData(self):
#         self.name = input("enter name")
#     def getData(self):
#         print(self.name)


# obj = Demo()

# obj.setData()
# obj.getData()







# class  Demo:
#     name = "hanu"

#     def setData(self):
#         self.age = 89
#     def show(s):
#         print(s.name)
#         print(s.age)


# obj = Demo()
# obj.setData()
# obj.show()



# list =[ 4,5,4,6]
# fun = [lambda x = i: x*5 for i in list ] 
# for i  in fun:
#       print(i())




#print(list(fun()))
# fun = lambda x,y :(x+y , x-y)
# print(fun(3,4))

#fun = lambda x , y :( "even" if x%2==0 else "old" ,"even" if y%2==0 else "old")
#fun = lambda x , y :( x if x>y else y ,x if x<y else  y)
#fun = lambda x , y ,z: x if x>y and x>z else y if y >z else z 
#fun = [lambda x = i: x for i in range(10) ] 

#print(fun())
# for i  in fun:
#      print(i())

#r = fun(5 ,14,53)
#print(r)
# print("max",r[0])
# print("min",r[1])

# def  fun (n):
#     if(n%2==0):
#         return "even"
#     else :
#         return "old"
# print(fun(4))

# fun = lambda x :x*3 # lambda 5 : 5*3 = 15
# print(fun(5))


# fun = lambda x : "even" if x%2==0 else "old"

# print(fun(6))

# s=lambda : print("hello")

# #print(s())
# s=lambda : "hello"

# print(s())



# def max1 (n1,n2):
#     if(n1 > n2):
#         return n1
#     else :
#         return n2 

# def min1 (n1,n2):
#     if(n1 < n2):
#         return n1
#     else :
#         return n2 

# print(max1(3,4))
# print(min1(3,4))


# print(max(4,5))
# print(min(4,5))