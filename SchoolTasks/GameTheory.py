# 1
def f(s, p):
    if p % 2 == 0 and s == '':
        return True
    if p % 2 != 0 and s == '':
        return False
    if p % 2 == 1:
        return any([f(s.replace(x, '', 1), p + 1) or f(s.replace(x, ''), p + 1) for x in set(s)])
    if p % 2 == 0:
        return all([f(s.replace(x, '', 1), p + 1) and f(s.replace(x, ''), p + 1) for x in set(s)])


a = ['ДА', 'АГА', 'СТО', 'МАМА', 'СССР', 'ОГОГО', 'ТАРТАР', 'ТОРТ', 'РОКОКО', 'РЕННЕР', 'АВАТАР', 'КАРАКУРТ', 'КАСКАД',
     'АНАТАНА', 'НЯННЯН', 'НАГАН']
for el in a:
    if f(el, 1) == True:
        print(el)
