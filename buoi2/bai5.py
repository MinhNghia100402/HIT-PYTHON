x = int(input())
a =b=c= 0
while x>=10:
    a+=int(x%10)
    x=int(x/10)
a+=x
if a<10:
    print(a)
else:
    while a>=10:
        b+=int(a%10)
        a= int(a/10)
    b+=a
if b<10:
    print(b)
else:
    while b>=10:
        c+=int(b%10)
        b= int(b/10)
    c+=b
    print(c)