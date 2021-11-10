a = list(map(int,input().split()))
for i  in a:
    if i%2==1:
        print(i,end=' ')
        a.remove(i)
print(a)