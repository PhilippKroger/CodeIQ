from math import log


def huffman_code(l):
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
    for i in range(len(snv) - 1, -1, -1):
        f_int.append(list(map(int, snv[i])))
        f_str.append(list(map(str, snv[i])))

    print(f_int)
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
    dk = list(d.keys())
    for i in range(len(f_str[-1])):
        lfstrx = len(f_str[-1][i]) - len(str(v[i]))
        xd = dk[i]
        yd = f_str[-1][i][-lfstrx:]
        d1[xd] = yd
    m = sum(list(v)) * round(log(len(dk), 2))  # I1
    n = 0  # I2
    for i in range(len(v)):  # I2 += I2
        n += (len(list(d1.values())[i]) * v[i])
    k = m / n

    return " 1) {} \n 2) {} бит \n 3) {} бит \n 4) {} ".format(d1, m, n, k)


inp = 'A 26 B 13 C 17 D 28'.split()
print(huffman_code(inp))


# A 26 B 13 C 17 D 28
# A 100 B 2 C 1

