from math import log


def huffman_code(l):
    """6 step solution"""
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

    f_int, f_str = [], []
    for i in range(len(snv)- 1, -1, -1):
        f_int.append(list(map(int, snv[i])))
        f_str.append(list(map(str, snv[i])))

    print(f_int)
    print(f_str)
    print('=' * 100)

    for i in range(len(f_int)):
        for j in range(i + 1, len(f_int)):
            #  skip [54, 30] [28, 26, 17, 13]
            if len(f_int[j]) // len(f_int[i]) == 2:
                continue
            else:
                # first iteration [54, 30]
                if len(f_int[i]) == 2:
                    f_str[i][0] += '0'
                    f_str[i][1] += '1'

                for x in range(len(f_int[j]) - 1):
                    for y in range(len(f_int[j]) - 1):
                        # 54 = 28 + 26
                        if f_int[i][x] == f_int[j][y] + f_int[j][y + 1]:
                            f_str[j][y] += str(f_str[i][x][-1] + '0')
                            f_str[j][y + 1] += str(f_str[i][x][-1] + '1')
                        else:
                            # 30 == 30 or 28 == 26 etc.
                            if f_int[i][x] == f_int[j][y]:
                                fy = len(f_str[i][x]) - len(f_str[j][y])
                                f_str[j][y] += str(f_str[i][x][-fy:])

    d1 = {}
    lfstr = f_str[-1]
    dk = list(d.keys())
    for i in range(len(lfstr)):
        lfstrx = len(lfstr[i]) - len(str(v[i]))
        xd = dk[i]
        yd = lfstr[i][-lfstrx:]
        d1[xd] = yd
    K1 = sum(list(v))
    I = round(log(len(dk), 2))
    I1 = K1 * I
    dd = list(d1.values())
    I2 = 0
    for i in range(len(dd)):
        I2 += (len(dd[i]) * v[i])
    k = I1 / I2

    return "1) {} \n 2) {} бит \n 3) {} бит \n 4) {} ".format(d1, I1, I2, k)


inp = 'A 100 B 2 C 1'.split()  # A 26 B 13 C 17 D 28
print(huffman_code(inp))
