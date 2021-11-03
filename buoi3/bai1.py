def check(a):
    if '0' in a or '1' in a:
        return True
    else:
        return False
def sosanh(a,b):
    first=set()
    second=set()
    for i in range(len(a)):
        if a[i]=='0' or a[i]=='1':
            first.add(i)
    for i in range(len(b)):
        if b[i]=='0' or b[i]=='1':
            second.add(i)
    if len(first^second)==0
        return True
    else:
        return False
def MyMathShower(a):
    for i in range(len(a)):
        if check(a[i])==True:
            sosanh()
