def road(n, k):
    """
    :param n: number of houses on the street
    :param k: from which house do we start bypassing the street
    :return: full path

    Example:
        Input: 8 1 / Output: 1 3 5 7 8 6 4 2
        Input: 7 6 / Output: 6 4 2 1 3 5 7
    """
    if n >= 4:
        print(n, k)
        x, y, r = [], [], []
        for i in range(1, n+1):
            if i % 2 == 0:
                y.append(i)
            elif i % 2 != 0:
                x.append(i)
        xy = [x, y]
        for i in range(len(xy)):
            if i == 0:
                print('x:', xy[i])
            else:
                print('y:', xy[i])
        k_ind = []
        k_ind_xy = ''
        for i in range(0, len(xy)):
            for j in range(0, len(xy[i])):
                if k == int(xy[i][j]):
                    k_ind.append(i)
                    k_ind.append(j)
                    if i == 0:
                        k_ind_xy += 'x'
                    else:
                        k_ind_xy += 'y'
        print('k coordinates:', k_ind, 'K in:', k_ind_xy, 'list.')
        y_rev, x_rev = list(reversed(y)), list(reversed(x))
        fl = 1
        if k_ind[0] == 0:  # k в X списке
            if k == int(x[0]) or k == int(x[1]):  # Дворник начинает мести по нечётным ул. слева направо
                for i in range(len(x)):
                    if fl == 1:
                        if i == k_ind[1]:
                            fl -= 1
                            r.append(x[i])
                    else:
                        r.append(x[i])
                for i in range(len(y_rev)):
                    r.append(y_rev[i])
            else:  # дворник начинает мести по нечётной улице справа налево
                for i in range(len(x_rev)):
                    if fl == 1:
                        if k == x_rev[i]:
                            fl -= 1
                            r.append(x_rev[i])
                    else:
                        r.append(x_rev[i])
                for i in range(len(y)):
                    r.append(y[i])
        elif k_ind[0] == 1:  # K в Y списке
            if k == int(y[0]) or k == int(y[1]):  # Дворник начинает мести по нечётным ул. слева направо
                for i in range(len(y)):
                    if fl == 1:
                        if k == y[i]:
                            fl -= 1
                            r.append(y[i])
                    else:
                        r.append(y[i])
                for i in range(len(x_rev)):
                    r.append(x_rev[i])
            else:  # дворник начинает мести по нечётной улице справа налево
                for i in range(len(y_rev)):
                    if fl == 1:
                        if k == y_rev[i]:
                            fl -= 1
                            r.append(y_rev[i])
                    else:
                        r.append(y_rev[i])

                for i in range(len(x)):
                    r.append(x[i])
        return r


n, k = map(int, input().split())
print(road(n, k))
