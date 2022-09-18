def run_length_encoding(a):
    """RLE"""
    a += '*'
    k = 0
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

    l = []

    for i in range(0, len(a), 8):
        l.append(a[i:i+8])

    x = ''
    for i in range(len(l)):
        ln = int(l[i][1:], 2)

        if l[i][0] == '1':
            x += str(ln)
            x += ln * chr(int(l[i+1], 2))
            continue
        elif l[i][0] == '0':
            x += str(ln)
            for j in range(ln):
                x += chr(int(l[i+1+j], 2))
    return x

print(de_rle('1000111111000000000000101100000111000010'))

