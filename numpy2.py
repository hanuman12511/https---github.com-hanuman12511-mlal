import numpy as np

ar = np.arange(1,9)
arr = np.array(ar)
ar1 = np.arange(11,19)
arr1 = np.array(ar1)


print(arr)
print(arr1)
# + ,- ,* / ,//, % ,**
# arr2 = arr**arr1
# print(arr2)

a = 2**3

print(a)


# print("arr=>",arr)

# arr2= arr.view()
# arr [2] =89

# print(arr2)
# print(arr)
# arr2= arr.copy()
# arr [2] =89

# print(arr2)
# print(arr)

# arr2 = arr

# print("arr2=>",arr2)

# new_arr = ar.reshape(4,2)



#print(new_arr)

# new_arr1 = new_arr.reshape(2,2,2)
# print(new_arr1) 

# for i in np.nditer(new_arr1):
#     print(i)
# for i in np.nditer(new_arr):
#     print(i)
        

# for i  in  new_arr:
#     print(i)

# for i in new_arr:
#     for j in i:
#         print(j) 

#print(ar.size)
# print(ar.shape)


# arr=[3,4,5,5,6,7,8,9]
# ar = np.array(arr)
#new_arr = ar.reshape(4,2)
# new_arr = ar.reshape(2,2,2)
# n_ar = new_arr.reshape(4,2)
# n_ar1 = n_ar.reshape(-1)


# print(n_ar1)








#bool_ar = (ar %2 ==0) & (ar<=6)
#bool_ar = (ar %2 ==0) | (ar<=6)

# print(ar)
# print(bool_ar)
# print(ar[bool_ar])

# bool_arr = ar>4
# print(bool_arr)

# print(ar[bool_arr])


# index = [1,3,6]
# data=  [12,34,56]
# print(ar)
# ar[index] = data
# print(ar)




#ar =[ [[3,4,5,5,6,7,8,9],[13,14,15,15,16,17,18,19]],[[23,24,25,25,26,27,28,29],[33,34,35,35,36,37,38,39]]]
#l1 = np.array(ar)

# print(l1[0:1,0:,1:])
# l1[0:1,0:,1:] =70


#print(l1[1:6:2])

#l1[0:2,1:5] = 50



# print(l1[1][2])
# print(l1[1,])
#print(l1[1:,])
#print(l1[0:2,])
#print(l1[0:2,1])
#print(l1[0:2,1:5])
# print(l1)
# print(l1[0])
# print(l1[2])
# print(l1[2:])
# print(l1[2:6])
# print(l1[:6])
# print(l1[:-1])
# print(l1[-4:-1])
# print(l1[-1:])
# print(l1[-4:])

# l1 [0] = 9
# l1 [-1] = 19
# l1 [-3:] = 30 #this is not run
# l1 [2:5] = 9   # this is not run
# print(l1)

#l1 = np.random.rand(6)
#l1 = np.random.randint(5)

#l1 = np.arange(1,7,2)

#print(l1)

# l1 = [3,4,5]
#ar = np.array(l1)

#ar = np.zeros(4)
#ar =np.zeros((2,3))
#ar =np.zeros((2,2,3))
#ar= np.ones(4)
#ar= np.ones((4,3))
#ar= np.ones((4,2,3))

#ar = np.empty(4)
#ar = np.empty((4,3))
#ar = np.empty((3,4,3))

#ar= np.full((2,3),4)
# ar= np.full((3,2,3),4)
# print(ar)