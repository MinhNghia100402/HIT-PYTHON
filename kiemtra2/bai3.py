import numpy as np
a = np.random.randint(2,9,size=(3,3))
b  = np.random.randint(10,20,size=(3,3))
c = a*b
print(a)
print(b)
print('a*b = ',c)
print('TBC = ',np.average(c))
print('max = ',np.amax(c))