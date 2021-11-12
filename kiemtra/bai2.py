a = list(map(int,input().split()))
dem=temp=0
for i in a:
    for j in range(1,i):
        if i % j == 0:
            dem += j
    if dem > i:
        temp += 1
        print(i,end=' ')
print("so luong = ",temp)