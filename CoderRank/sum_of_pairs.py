def sum_pairs(ints, s):
    l = []
    l_ind = []
    for i in range(0, len(ints)):
        for y in range(i+1, len(ints)):
            if ints[i] + ints[y] == s:
                a = ints[i]
                b = ints[y]
                l.append(a)
                l.append(b)
                l_ind.append(ints.index(ints[i]))
                l_ind.append(ints.index(ints[y]))
                print(l, l_ind)


print(sum_pairs([10, 5, 2, 3, 7, 5],  10))