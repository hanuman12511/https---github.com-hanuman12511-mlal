import numpy as np


l1 = [3,4,5]
l2 = [4,5,6]
l3 = [5,8,9]
l4 = [2,3,4]

ar = np.array([[l1,l2],[l3,l4]])
print(ar.dtype)
print(ar.size)
print(ar.shape)
#print(ar[0,0,2])


ar[0,0,2] = 10

print(ar*2)

# dtype , size ,shape

#ar = np.array([l1,l2])
#print(ar)
#print(ar.size)
#print(ar.shape)
# print(ar[0,0])
# print(ar[-1,-1])
# ar[0,0] = 9
# print(ar)

# arr = 3*ar
# print(arr)


#print(np)
#1d
# list = [2,3,4,6]
# ar = np.array(list)
# print(ar)
# print(ar[0])
# print(ar[-1])

# ar[0] =5
# print(ar)

# data = (2,3,4,5)

# ar = np.array(data)

# print(ar.dtype)
#print(ar)
#arr = ar+4
#print(arr)

# arr = ar-2

# arr = ar*2
# arr = ar/2
# print(arr)
# print(arr.dtype)