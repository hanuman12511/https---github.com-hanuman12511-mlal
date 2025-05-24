import pandas as pd
df = pd.read_csv('test.csv')


dff = pd.DataFrame(df)

#dff[col]
#loc[rowlabel]
#1loc[rowindex]

# print(dff["Player"])
# print(dff.loc[1])
# print(dff.iloc[1])
#print(df.head())
# print(df.head(20))
# print(df.tail(20))
#print(df.loc[1])
#print(df.loc[[1,3]])
#print(df.loc[[1,3,20]])
#print(df.loc[100:200])
#print(df.loc[100:200,["Player","Mat","Runs"]])
#print(df.loc[100:200,"Player":"Runs"])
#print(df.loc[100:200:10,"Player":"Runs":2])
#loc[row,col]
#row (start:end:step)
#col (start:end:step)
# print(df.loc[:200,:"Runs"])

# df1 = df.loc[:200,"Player":"Mat"]
#df2 = df.loc[:200,"HS":"50"]
#df2 = df.loc[:200,:-1]
df2 = df.iloc[:200,:-1]
# print(df2["Player"])
print(df2.loc[10:20,"Mat"].values.reshape((-1,1)))
# import numpy as np

# arr1 = np.array(df2.loc[10:20,"Mat"].values)
