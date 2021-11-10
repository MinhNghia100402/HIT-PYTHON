def nhap():
    print('nhap mang a ')
    a = list(map(int,input()))
    print('nhap phan tu x ')
    b = int(input())
    return a,b
def Remove():
    for i in arr:
        if i==x:
            arr.remove(i)
            break
    return arr
def Removeall():
    for i in arr:
        if i==x:
            arr.remove(i)
    return arr
def add():
    print('nhap vi tri can chen')
    y=int(input())
    if y<0 or y>len(arr):
        print('vi tri chen khong hop le')
    else:
        arr.insert(y,x)
    print('sau khi chen la :',arr)
arr,x =nhap()
print(Remove())
print(Removeall())
add()