from itertools import product
k = 0
for x in product('01234567', repeat=4):
    s = ''.join(x)
    if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3] and s[3]!=s[4]:
        k += 1
print(k)
