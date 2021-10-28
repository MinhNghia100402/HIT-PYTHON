
x = input('ý a, nhập chuỗi ')
a = len(x)
while (a<10):
    print('nhập lại chuỗi x ')
    x = input()
    a = len(x)
print('độ dài chuỗi là : ' ,a)
L = list(x)
print(L[2:6])
y = input('ý b , nhap chuỗi   >> ')
y = y.upper()
print(y)
y=y.lower()
print(y)
y=y.replace('b','g')
print(y)
z = 'hElLo-mY-NAMe-iS-SuZIe'
z=z.lower()
z=z.replace('-',' ')
z=z.title()
print(z)




