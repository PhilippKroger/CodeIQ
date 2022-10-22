n = int(input())

# перевод в троичную
b = ''
while n > 0:
    b = str(n % 3) + b
    n = n // 3
#print(b)


l = []
for i in range(0, len(b)-2):
    l.append(int(b[i:i+3]))
    #print(b[i:i+3])
#print(l)

k = 0
for i in range(len(l)):
    if l[i]==120:
        k += 1


if k < 1:
    print(0)
elif k == 1:
    x = ''.join(map(str, l))
    #print(x)
    x = x[::-1]
    #print(x)
    rez = 0
    for i in range(0, len(x) - 2):
        if x[i:i + 3] == '021':
            rez = i
            #print(i)
        #print(x[i:i + 3])
    print(rez - 1)
else:
    b = b[::-1]
    #print(k)
    r = 0
    for i in range(0, len(b)-2):
        if b[i:i+3] == '012':
            r = i
            break
    print(r+1)