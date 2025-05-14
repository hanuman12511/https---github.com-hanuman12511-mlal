list=[8,9]

print(list.index(9));

# import pandas 
# import pandas  as pd
# from pandas import *
# from pandas import DataFrame
# s1 = {"course":"cs","sub":["sub1","sub2","sub3"]}

# df = DataFrame(s1)
# print(df)


# team1 = ["uu1","uu2"]
# project1 ={"p1":team1}
# tp1 = {"user1":["it","user1@g.c","9999988898",project1]}
# tp2 = {"user2":["test","user2@g.c","9999988898",project1]}
# tp3 = {"user3":["design","user3@g.c","9999988898",project1]}

# info = [tp1,tp2,tp3]




# s2 = {"course":"EE","sub":["sub1","sub2","sub3"]}

# sname = {"hanu":[s1,"hanu@gmail.com","9898989898"],"ram":[s1,"ram@gmail.com","9898989898"],"raj":[s2,"raj@gmail.com","989898989"]}

# info = {"name":sname}

# #print(info)
# #print(info['name']['ram'])

# # name course email phone output
# for key ,value in info.items():
#     print(value)
#     print("*****************")
#     for key2 ,value1 in value.items():

#         print(value1)
#         for key1,value2 in value1.items():
#             if(key1 == "course"):
#                 print(key2,value2)













#dict  = {key:value}

#dataset = {"id":100,"emp_name":"user1","age":30,"phone":"9898787878"}
#dataset = {"id":[100,200],"emp_name":["user1","user2"],"age":[30,35],"phone":["9898787878","9898987878"]}
# list = []
# pos=0
# flist = []
# for data in dataset.items():
#     list.append(data[1])
#print(list)
# for i in range(len(list[0])):
#     list1=[]
#     for j  in list:
#         #print(j[i])
#         list1.append(j[i])
#     flist.append(set(list1))

# print(flist)

# print(data[1])
    # data1 = data[1]
    # print(data1[pos])
    # if(pos < len(data1)):
    # pos+=1
    # list.append(set(data1))
#print(list)
#data = ('id',[100,200])
#print(data[1])

#setdata = {100 , "user1",30 ,"9898787878"}
#list [{100 , "user1",30 ,"9898787878"}]

#print(setdata)



#dataset1 = {"dept":"it"}

# print(dataset)

# name = input("enter name")
# pos = ""
# for key in dataset:
#     if(key == "emp_name"):
#         for i in range(len(dataset[key])):
#             if(name == dataset[key][i]):
#                 pos =i
#                 break


# for key in dataset:
#     print(key ,dataset[key][pos])
   

# if name in dataset['emp_name']:
#     print("name found")
# else:
#     print("not")

# dataset.update(dataset1)
# print(dataset)

#print(dataset.fromkeys(['age']))


#print(dataset.get('age'))
#print(dataset)

# dataset.clear()

# dataset1 = dataset.copy()
# print(dataset1)


# print(dataset['emp_name'])

# key = input("enter key")
# value = input("enter dpt")


# dataset.update({key:value})

# print(dataset)




# key = input("enter key")
# value = input("enter dpt")

# dataset[key] =value
# print(dataset)

# key = input("enter key")
# del dataset[key]
# print(dataset)


# for value in dataset:
#     print(value)

# for value in dataset.values():
#     print(value)

# for value in dataset.keys():
#     print(value)

# for value in dataset.items():
#     print(value)

# key = "age"
# print(dataset.pop(key))
# print(dataset)

#key = "age"
# print(dataset.popitem())
# print(dataset)


