def nhap():
    print('nhap mang a ')
    a = list(map(int,input()))
    return a
def dem():
    for i in set(arr):
        c = arr.count(i)
        print(i, ":",c)
arr =nhap()
dem()