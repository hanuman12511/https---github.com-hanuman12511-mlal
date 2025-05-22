import pandas as pd
import numpy as np

# index= ["r1","r2","r3"]
df =pd.DataFrame(np.array([np.random.rand(6),np.random.rand(6),np.random.rand(6)]) )

print(df)
# print(df[2])
# print(df[2][2])
# print(df[1:])
# print(df[1:,2:])
print(df.loc[1:2,1])
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
