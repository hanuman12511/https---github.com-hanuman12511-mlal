import numpy as np

data = ["user1","Uesrs2","USER3"]
data1 = ["4","5","6"]
arr1 = np.array(data1)
arr = np.array(data)
ar = np.char.add(arr1,arr)
ar = np.char.capitalize(arr)
ar1 = np.char.islower(arr)
ar1 = np.char.lower(arr)
ar1 = np.char.upper(arr)
ar1 = np.char.title(arr)
ar1 = np.char.str_len(arr)
ar1 = np.char.center(arr,width=10)
ar1 = np.char.count(arr,"U")
ar1 = np.char.join(arr,"U")
ar1 = np.char.replace(arr,"U","u")
ar1 = np.char.multiply(arr,4)
ar1 = np.char.split(arr,"e")
print(arr)
ar1 = np.char.less(arr,"ue")


# s = "user"
# print(s*3)
print(ar1)
#print(ar[ar1])

# data = [
#     [3,1,2],
#     [4,5,6],
#     [1,2,3],
#     [7,8,0],
#         ]
#data =[4,3,5,7]
#print(np.max(data))


# ar = np.array(data)
# ar.sort( axis=0)
# print(ar)
# arrt = ar.T
# #print(ar.T)
# print(arrt)
# print(ar.transpose())
