a = int(input())
b= int(input())
n = int(input())
c = {}
for i in range(a,b+1):
    if i%n==0:
        c[i]=i*i
print(c)
