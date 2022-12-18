n = input()
l = []
for i in range(len(n)):
    if n[i] not in l:
        l.append(n[i])
int_n = int(n, 5)
int_l = []
for i in range(len(str(int_n))):
    if str(int_n)[i] not in int_l:
        int_l.append(str(int_n)[i])
if len(set(int_l) ^ set(l)) > 0:
    print(len(set(int_l).difference(set(l))))
elif len(set(int_l)) == len(set(l)):
    print(0)