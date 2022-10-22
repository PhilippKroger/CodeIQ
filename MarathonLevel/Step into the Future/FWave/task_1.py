n = int(input())
ns = str(n)
nl = []
for i in range(len(ns)):
    nl.append(int(ns[i]))
nl1 = nl.copy()
m = max(nl)
for i in range(len(nl)):
    if nl[i] == m:
        nl[i] = nl[i]+3
nl1 = int(''.join(map(str, nl1)))
nl2 = int(''.join(map(str, nl)))
print(nl2-nl1)