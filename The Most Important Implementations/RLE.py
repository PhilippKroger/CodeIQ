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
    s2 = ''
    a.append('00000000')
    for i in range(0, len(a)-1):
        if a[i][0] == '1':
            s2 += (chr(int(a[i+1], 2)) * int(a[i][1:], 2))
            continue
        if a[i][0] == '0':
            s2 += chr(int(a[i+1], 2) * int(a[i][1:], 2))
    return s2


# print(de_rle(['10001111', '01000001', '00000010', '01000010', '01000011']))  #АААААААААААААААБВ



def r(s):
    l = []
    xl = ''
    for i in range(0, len(s), 8):
        l.append(s[i:i+8])
    l.append('00000000')
    print(l)
    for i in range(len(l)-1):
        print(l[i])
        if l[i][0] == '1':
            xl += int(l[i][1:], 2) * chr((int(l[i+1], 2)))
            print(int(l[i][1:],2))
            l.pop(i+1)

        if l[i][0] == '0':
            print(chr(int(l[i], 2)) )
            k = int(l[i][1:], 2)
            xl += str(int(l[i][1:], 2))
            #xl += str(int(l[i], 2))
            for j in range(i+1, k ):
                print(j)
                xl += chr(int(l[i], 2))
    return xl

print(r('1000111101000001000000100100001001000011'))
