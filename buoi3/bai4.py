A = {'An','Bình','Nam','Long','Ngọc','Tu'}
B = {'Bình','Linh','Nam','Hai','Long'}
A.remove('Tu')
A.add('Cuong')
C = A.union(B)
X =A&B
D=A | B
D.update(X)
E = A-B
F = A^B
print(C)
print(D)
print(E)
print(F)
