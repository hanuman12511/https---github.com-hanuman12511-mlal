import numpy as np
def NArray(n):
    #data=np.random.rand(n,n)
    data=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if((i+j)%2==0 ):
                    data[i][j] = 2
            else :
                    data[i][j] = 1
    print(data)
                 
NArray(5)

# data = np.random.randint(1,29,size = (3,3,3))
# print(data)
# data[np.where(data%2==0 )]=89
# print(data)
#print(data[np.where(data>12 )])


# print(np.max (data,axis=1))

# for i in np.max (data,axis=1).flat:
#     print(i)

# for i in data.flat:
#       print("flat",i)

# for i in np.nditer(data):
#      print("nditer",i)