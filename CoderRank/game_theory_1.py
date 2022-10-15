# +1 / +2 / *2
def f(a, p, r1, r2):
    if a >= 21 and (p == 2 or p == 4):
        return True
    if a < 21 and p == 4:
        return False
    if a >= 21 and p == 2:
        return False
    if p % 2 == 1:
        if r1 == 0:
            return f(a + 1, p + 1, 1, r2) or f(a + 2, p + 1, 2, r2) or f(a * 2, p + 1, 3, r2)
        if r1 == 1:
            return f(a + 2, p + 1, 2, r2) or f(a * 2, p + 1, 3, r2)
        if r1 == 2:
            return f(a + 1, p + 1, 1, r2) or f(a * 2, p + 1, 3, r2)
        if r1 == 3:
            return f(a + 1, p + 1, 1, r2) or f(a + 2, p + 1, 2, r2)
    if p % 2 == 0:
        if r2 == 0:
            return f(a + 1, p + 1, r1, 1) and f(a + 2, p + 1, r1, 2) and f(a * 2, p + 1, r1, 3)
        if r2 == 1:
            return f(a + 2, p + 1, r1, 2) and (a * 2, p + 1, r1, 3)
        if r2 == 2:
            return f(a + 1, p + 1, r1, 1) and f(a * 2, p + 1, r1, 3)
        if r2 == 3:
            return f(a + 1, p + 1, r1, 1) and f(a + 2, p + 1, r1, 2)


for s in range(1, 21):
    if f(s, 1, 0, 0):
        print(s)
