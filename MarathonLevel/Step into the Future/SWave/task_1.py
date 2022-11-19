def f(a):
    a1 = a
    b = []
    while a > 0:
        b.append(a % 10)
        a = a // 10
    b = b[::-1]
    m = min(b)
    for i in range(len(b)):
        if b[i] == m:
            b[i] += 3
    nb = int(''.join(map(str, b)))
    return nb - a1


a = int(input())
print(f(a))

"""
Write a program that will determine how much a number will change if the minimum value of the digit included in it,
increase by 3.
Input: natural number in decimal notation, not exceeding 109.
The number cannot contain the digits 7, 8 and 9.
Output: the difference between the number obtained in accordance with the task, and the original number.

Example:
Input data Output data
1234       3000
163205     30
"""

"""
Написать программу, которая определит, насколько изменится число, если минимальную по значению цифру, входящую в него,
увеличить на 3.
Входные данные: натуральное число в десятичной системе счисления, не превышающее 109.
В числе не может быть цифр 7, 8 и 9.
Выходные данные: разность между числом, полученным в соответствии с заданием, и исходным числом.

Пример:
Входные данные  Выходные данные
1234            3000
163205          30
"""