
a = list(map(int,input().split()))
temp=0
for i in a:
    dem=0
    for j in range(2, i - 1):
        if i % j == 0:
            dem += 1
    if dem == 0:
        temp+=1
print(temp)