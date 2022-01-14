a = list(map(int,input().split()))
b = set(a)
d =[]
for i in b:
    c = []
    for j in a:
        if j==i:
            c.append(j)
    d.append(c)
print(d)
