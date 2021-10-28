a = list(map(int,input().split()))
x = len(a)
b = 0
for i in range(x):
    b+= int(a[i])
    a[i] = b
print(a)
