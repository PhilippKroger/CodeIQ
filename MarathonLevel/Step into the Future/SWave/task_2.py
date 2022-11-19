def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n = n // 4
    a = int(s)
    b = []
    while a > 0:
      b.append(a % 10)
      a = a // 10
    b = b[::-1]
    a = b.count(3)
    return a


n = int(input())
print(f(n))


"""
For some decimal number, determine how many digits 3 contains its entry in the quaternary number system.
Input: natural number in decimal s/s, not exceeding 109.
Output data: the number of digits 3 in the 4th s / s.

Example:
Input data Output data
390        0
219        2
"""

"""
Для некоторого десятичного числа определить, сколько цифр 3 содержит его запись в четверичной системе счисления.
Входные данные: натуральное число в десятичной с/с, не превышающее 109.
Выходные данные: количество цифр 3 в 4-й с/с.

Пример:
Входные данные Выходные данные
390            0
219            2
"""