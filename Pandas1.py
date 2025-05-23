import pandas as pd
import numpy as np


id=[1,2,3,4,5]
name=["user1","user2","user3","user4","user5"]
age = [22,33,44,55,66]


df = pd.DataFrame([id,name,age],index=["id","name","age"],columns=["c1","c2","c3","c4","c5"])


print(df)
# print(df.loc["id"].values.reshape((-1,1)))
# print(df.loc[["id","name"]])
# print(df.loc[:,"c2"])
print(df.loc["name","c2"])
print(df.loc["age","c2"])
print(df.loc[["name","age"],["c2","c4"]])
print(df.loc[["name","age"],"c2":])
print(df.loc[["name","age"],:"c4"])

# print(df)
# df["c5"] = [6,"user5",23]
# print(df)
# print(df['c2'])
# print(df["id"::2])
# df[:"salary"] = [22,55,55,5,5]

# df.update({"age":[30,303,303,404,40]})
# pd.concat(df,pd.DataFrame([{"salary":[30,303,303,404,40]}]))
# print(df)

# x= np.linspace(-4,4,9)
# y= np.linspace(-5,5,11)

# x1,y1 = np.meshgrid(x,y)

# print(x1)
# print(y1)


# index= ["r1","r2","r3"]
# df =pd.DataFrame(np.array([np.random.rand(6),np.random.rand(6),np.random.rand(6)]) )

# print(df)
# print(df[2])
# print(df[2][2])
# print(df[1:])
# print(df[1:,2:])
# print(df.loc[1:2,1])
# dict1= {"id":[1,2,3,4],"name":["a","b","c","d"],"salary":[2,3,4,5]}

# df = pd.DataFrame(data=dict1)
# print(df)


# print("size",df.size)
# print("shape",df.shape)
# print("info",df.info)
# print("index",df.index)
# print("value",df.values) 
# print("ndim",df.ndim)
# print("describe",df.describe)

# data = np.random.rand(6)
# s= pd.Series(data)
# index = ["r1","r2","r3","r4","r5","r6"]
# s= pd.Series(data,index=index)


# print(s)
# print(s['r2'])
# print("dtype",s.dtype)
# print("size",s.size)
# print("shape",s.shape)
# print("info",s.info)
# print("index",s.index)
# """ print("value",s.value) """
# print("ndim",s.ndim)
# print("describe",s.describe)

#print(s)
#print(s[2])
#s[2] = 7
#print(s.info)
