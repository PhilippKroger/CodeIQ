

d = {'T': 50, 'H': 53, 'E': 72, 'O': 89, ' ': 179}
v = sorted(d.values(), reverse=True)
nv = v.copy()
snv = []
print(nv)
for i in range(len(nv)-1):
    nv.sort(reverse=True)
    nv1 = list(map(int, nv))
    snv.append(list(nv1))
    x = sum(nv[-2:])
    nv.pop()
    nv.pop()
    nv.append(x)
    print(nv)
print(snv)


f = []
fl = {}
for i in range(len(snv)-1, -1, -1):
    f.append(list(map(str, snv[i])))


# Прохождение по массиву, состоящего из подмассивов
for i in range(len(f)):
    print(f[i])
    if len(f[i]) == 2:
        fl[f[i][0]] = '0'
        fl[f[i][1]] = '1'

    if len(f[i]) > 2:
        pass

print(f)
print(fl)