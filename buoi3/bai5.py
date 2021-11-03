def MyMathPower(a):
    s=t=0
    p=1
    for i in a:
        s+=i
        t-=i
        p*=i
    print('tong = ',s)
    print('hieu = ',t)
    print('tich = ',p)
MyMathPower(a=list(map(int, input().split())))