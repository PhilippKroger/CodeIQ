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
