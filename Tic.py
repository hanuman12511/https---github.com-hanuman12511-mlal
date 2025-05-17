import numpy as np

pi = np.pi;

print(pi);
#x = np.arange(0,pi,10)
x= np.linspace(0,pi/2,20)
#x= np.linspace(1,10,5)
print(x)

y = np.sinh(x)
y = np.cosh(x)
y = np.tanh(x)
print(y)
# y = np.sin(x)
# y1 = np.cos(x)
# y2 = np.tan(x)

# print("sin",y)
# print("cos",y1)
# print("tan",y2)
