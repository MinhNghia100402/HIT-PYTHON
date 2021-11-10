a = input()
b = int(input())
c = a[b:len(a)]
d = reversed(c)
f = "".join(d)
e=a[0:b]
print(e+f)