from itertools import product

k = 0
for x in product('КУМА', repeat=5):
    s = ''.join(x)
    if s[0] in 'КМ' and s[-1] in 'УА':  # s[-1] - last symbol
        k += 1
print(k)

k = 0
for x in product('КМ', 'КУМА', 'КУМА', 'КУМА', 'УА',):
    s = ''.join(x)
    k += 1
print(k)
