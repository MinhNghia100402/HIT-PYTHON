a = input()
if len(a)<=10:
    print(a)
else:
    b=list(a)
    c= b[:1]+[len(a[1:len(a)-1])] +b[len(a)-1:]
    for i in c:
        print(i,end='')