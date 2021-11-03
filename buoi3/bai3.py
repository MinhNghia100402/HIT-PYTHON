a = input()
b = input()
j = 0
for i in a:
    if i == len(b):
        break
    if i == b[j]:
        j+=1
if j == len(b):
    print('la tap hop  con')
else:
    print('khong la tap hop con')