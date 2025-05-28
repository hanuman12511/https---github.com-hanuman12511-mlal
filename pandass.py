import pandas as pd

df  = pd.read_csv('asiacup.csv').head()

#df1 = df[['Team','Run Scored']].where(df['Run Scored']>100)
df1 = df[['Team','Run Scored']].query("`Run Scored`>100")
df1= df.groupby('Team')['Run Scored'].agg(['min','max'])

# df1 = df[['Team', 'Run Scored']].where(df['Run Scored'] > 100).dropna()
# df_clean = df.dropna()
#df1 = df.loc[:,['Team', 'Run Scored']].where(df['Run Scored'] > 100).dropna()

# print(df_clean)
print(df1)


#print(df.groupby(['Team'], sort=False)['Run Scored'].sum().reset_index())


#print(df[df['Run Scored']>20])