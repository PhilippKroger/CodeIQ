from math import log

# l = input().split()
#l = 'A 26 B 13 C 17 D 28'.split()
l = 'A 100 B 2 C 1'.split()
d = {}
for i in range(0, len(l), 2):
    d[l[i]] = int(l[i + 1])

v = sorted(d.values(), reverse=True)
nv = v.copy()
snv = []
print(nv)
for i in range(len(nv) - 1):
    nv.sort(reverse=True)
    nv1 = list(map(int, nv))
    snv.append(list(nv1))
    x = sum(nv[-2:])
    nv.pop()
    nv.pop()
    nv.append(x)


fint = []
fstr = []
for i in range(len(snv) - 1, -1, -1):
    fint.append(list(map(int, snv[i])))
    fstr.append(list(map(str, snv[i])))

print(fint)
print(fstr)
f1 = fint.copy()
print('='*100)
for i in range(len(fint)):
    for j in range(i+1, len(fint)):
        #  skip [54, 30] [28, 26, 17, 13]
        if len(fint[j]) // len(fint[i]) == 2:
            continue
        else:
            if len(fint[i]) == 2:
                fstr[i][0] += '0'
                fstr[i][1] += '1'

            for x in range(len(fint[j])-1):

                for y in range(len(fint[j])-1):
                    if fint[i][x] == fint[j][y] + fint[j][y+1]:
                        fstr[j][y] += str(fstr[i][x][-1] + '0')
                        fstr[j][y+1] += str(fstr[i][x][-1] + '1')

                    else:
                        # 30 == 30 or 28 == 26 etc.
                        if fint[i][x] == fint[j][y]:
                            fy = len(fstr[i][x]) - len(fstr[j][y])
                            fstr[j][y] += str(fstr[i][x][-fy:])
                            """
                            print('fint[i][x]', fint[i][x], 'fint[j][y]', fint[j][y], 'fstr[i][x]', fstr[i][x],
                             'fstr[j][y]', fstr[j][y])
                            print(len(fstr[i][x]), len((fstr[j][y])))
                            print(str(fstr[i][x][-fy]))
                            """


d1 = {}
lfstr = fstr[-1]
dk = list(d.keys())
for i in range(len(lfstr)):
    lfstrx = len(lfstr[i]) - len(str(v[i]))
    xd = dk[i]
    yd = lfstr[i][-lfstrx:]
    d1[xd] = yd
print('1)', d1)

K1 = sum(list(v))
I = round(log(len(dk), 2))
I1 = K1 * I
print('2)', I1, 'бит')

dd = list(d1.values())
I2 = 0
print(dd)
for i in range(len(dd)):
    I2 += (len(dd[i]) * v[i])
print(I2)

k = I1 / I2
print(k)

"""
dkl = len(dk) # N
# i = >>>
i = int(log(dkl, 2))
#print(i)

k = sum(list(v))
#print(k)
I1 = k * i
print('2)', I1 ,'бит')

I2 = 0
#print(d)
d_values = list(d.values())
d1_values = list(d1.values())

#print('d1_values', d1_values)
#print('d_values', d_values)
for i in range(len(d1_values)):
    I2 += (len(d1_values[i])*d_values[i])
print('3)', I2 ,'бит')

print('4)', I1/I2)
"""
