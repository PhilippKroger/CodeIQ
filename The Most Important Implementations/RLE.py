def run_length_encoding(a):
    """RLE"""
    a += '*'
    k = 1
    x = ''
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            k += 1
        else:
            x += str(k) + a[i]
            k = 1

    """Compression ratio"""
    I = 0
    for i in range(len(x)):
        if not x[i].isdigit():
            I += 1
    K = len(x) / (I * 2)
    return 'RLE:', x, 'Compression ratio:', K


print(run_length_encoding('ABBCCCDDDD'))


def de_rle(a):
    #a = []
    s2 = ''
    #for i in range(0, len(s), 8):
    #    a.append(s[i:i + 8])
    a.append('00000000')
    print(a)
    for i in range(0, len(a)-1):
        if a[i][0] == '1':
            s2 += (chr(int(a[i+1], 2)) * int(a[i][1:], 2))
            continue
            #  a.pop(i+1)
        if a[i][0] == '0':
            s2 += chr(int(a[i+1], 2) * int(a[i][1:], 2))
    return s2


print(de_rle(['10001111', '01000001', '00000010', '01000010', '01000011']))  #АААААААААААААААБВ
#                15            A           2          Б           В
"""
            for j in range(i, i+1):
                x += chr(int(l[j], 2))
                print(chr(int(l[j], 2)))
            """

"""
l = []
    for i in range(0, len(a), 8):
        l.append(a[i:i + 8])
    x = ''

    for i in range(len(l)+1):
        ln = int(l[i][1:], 2)

        if l[i][0] == '0':
            pass
        elif l[i][0] == '1':
            x += str(ln)
            x += ln * chr(int(l[i+1], 2))
            continue
        else:
            pass
        print(x)
"""
