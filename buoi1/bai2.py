import math
print('nhập x ')
x=float(input())
s=(x*x+ pow(math.e,x)+math.sin(x))/(math.sqrt(x*x+1))
print('F(x) = ')
print(s)