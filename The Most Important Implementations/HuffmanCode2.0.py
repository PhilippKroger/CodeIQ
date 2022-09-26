from math import log

def hummong_code(l):
    #l = input().split()
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
    print('=' * 100)
    for i in range(len(fint)):
        for j in range(i + 1, len(fint)):
            #  skip [54, 30] [28, 26, 17, 13]
            if len(fint[j]) // len(fint[i]) == 2:
                continue
            else:
                if len(fint[i]) == 2:
                    fstr[i][0] += '0'
                    fstr[i][1] += '1'

                for x in range(len(fint[j]) - 1):

                    for y in range(len(fint[j]) - 1):
                        if fint[i][x] == fint[j][y] + fint[j][y + 1]:
                            fstr[j][y] += str(fstr[i][x][-1] + '0')
                            fstr[j][y + 1] += str(fstr[i][x][-1] + '1')

                        else:
                            # 30 == 30 or 28 == 26 etc.
                            if fint[i][x] == fint[j][y]:
                                fy = len(fstr[i][x]) - len(fstr[j][y])
                                fstr[j][y] += str(fstr[i][x][-fy:])

    d1 = {}
    lfstr = fstr[-1]
    dk = list(d.keys())
    for i in range(len(lfstr)):
        lfstrx = len(lfstr[i]) - len(str(v[i]))
        xd = dk[i]
        yd = lfstr[i][-lfstrx:]
        d1[xd] = yd
    print('1)', d1)
    dkl = len(dk)  # N
    i = int(log(dkl, 2))
    k = sum(list(v))
    I1 = k * i
    print('2)', I1, 'бит')
    I2 = 0
    d_values = list(d.values())
    d1_values = list(d1.values())

    for i in range(len(d1_values)):
        I2 += (len(d1_values[i]) * d_values[i])
    print('3)', I2, 'бит')
    print('4)', I1 / I2)
    return

l = input().split()
print(hummong_code(l))