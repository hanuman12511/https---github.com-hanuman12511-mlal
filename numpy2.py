import numpy as np

ar=[3,4,5,5,6,7,8,9]
#ar =[ [[3,4,5,5,6,7,8,9],[13,14,15,15,16,17,18,19]],[[23,24,25,25,26,27,28,29],[33,34,35,35,36,37,38,39]]]
l1 = np.array(ar)

# print(l1[0:1,0:,1:])
# l1[0:1,0:,1:] =70


print(l1[1:6:2])

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