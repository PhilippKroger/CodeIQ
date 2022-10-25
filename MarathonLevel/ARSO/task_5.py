
N=int(input())
a= []
s={}
p={}
for i in range(N):
    w=input()
    w=list(w)
    a.append(w)

for i in range(N):
    for j in range(N):

        if a[i][j]=='#':
            if i not in s:
                s[i]=[j]
            else:
                s[i].append(j)
        if a[i][j]=='.':
            if i not in p:
                p[i]=[j]
            else:
                p[i].append(j)
e=[x[-1] for x in a]
if '.' in e:
    e=e.index('.')
i=list(s.values())
p=list(p.values())
for x in range(len(i)):
    i[x]= tuple(i[x])

i=len(set(i))
for x in range(len(p)):
    p[x]= tuple(p[x])
o=len(set(p))
if i ==1:
    print('I')

elif o ==1 and all([x[0]=='#' and x[-1]=='#' for x in a]) and  set(a[0])==set('#') and set(a[-1])==set('#'):
    print('O')
elif o==1 and any([x[-1]=='.' for x in a]) and all([x[0]=='#' for x in a]) and set(a[0])==set('#') and set(a[-1])==set('#'):
    print('C')
elif o==1 and any([set(x)==set('#') for x in a[1:-1]]) and all([x[0]=='#' and x[-1]=='#' for x in a]):
    print('H')
elif o==1 and all([x[0]=='#'  for x in a]) and set(a[-1])==set('#') and any([x[-1]=='.' for x in a]) and len(set(a[0]))==2:
    print('L')
elif o==2 and set(a[0])==set('#') and set([x[0] for x in a])=='#' and '.' in [x[-1] for x in a] and set([ x[-1] for x in a[:e]])=='#' and set([ x[-1] for x in a[e:]])=='.':
    print('P')
else:
    print('X')
