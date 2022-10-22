n, m = 3, 3
"""l = []
for i in range(n):
    l.append([int(input()) for _ in range(m)])
print(l)"""
"""
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(l)):
    print(*l[i])

sx = []
for i in range(len(l)):
    sx.append(sum(l[i]))

sy = []
for i in range(len(l)):
    for j in range(len(l)):
        pass
"""

x=[[1, 1, 9, 1], [1, 2, 1, 3], [5, 5, 1, 1], [1, 1, 1, 1]]
for i in range(len(x)):
    print(*x[i])
y = []
z = []
for i in range(len(x)):
    stroki = 0
    for j in range(len(x[0])):
        stroki += x[i][j]  # вывод суммы отдельной строки
    y.append(stroki)  # с занесением в одномерный массив

for i in range(len(x[0])):
    stowbtsy = 0
    for j in range(len(x)):
        stowbtsy += x[j][i]  # вывод суммы отдельного столбца
    z.append(stowbtsy)  # с занесением в одномерный массив

print(y)
print(z)
r=list(set(y) & set(z))
print(r)
if len(r) == 0:
    print('NO')
else:
    pass

ry = y.index(r[0])
rz = z.index(r[0])
print(ry)
print(rz)

for i in range(len(x)):
    for j in range(len(x)):
        #print(x[ry][i], x[j][rz])
        x[ry][i], x[j][rz] = x[j][rz], x[ry][i]

for i in range(len(x)):
    print(*x[i])