def f(d, sn):
    sns = ''
    for i in range(len(sn)):
        sns += str(d.get(sn[i])) + ' '
    sns = sns.split()
    a = [int(x) for x in sns]
    N = len(a)
    k = 0
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                k += 1
    return k


alf = int(input())
d = {}
for x in range(alf):
    inp = input().split()
    d[inp[0]] = int(inp[1])
sn = input()
print(f(d, sn))


"""
Petya studies sorting algorithms. To better understand how bubble sort works,
he decided to arrange the array of letters not alphabetically, but in some arbitrary sequence
(for example, in the order of the letters on the keyboard, or any other).
Petya also wants to know how many character permutations are required to perform sorting.

Input: the first line contains a natural N, not exceeding 26 - the number of letters of the Latin alphabet,
that may occur in the sorted array. Next, in N lines, a space-separated capital Latin letter and
the number corresponding to the order of this letter from Petya's point of view. Next - a line of capital Latin letters,
by length not exceeding 100, for which it is required to calculate the number of permutations when sorting by bubble in ascending order

Output: number of element permutations.

Example:
Input data Output data
3
A 3
B 2        3
Z1
ABZ
"""

"""
Петя изучает алгоритмы сортировки. Чтобы лучше разобраться в работе сортировки пузырьком,
он решил упорядочить массив букв не по алфавиту, а в некоторой произвольной последовательности 
(например, в порядке расположения букв на клавиатуре, или любой другой).
Также Петя хочет узнать, сколько перестановок символов для выполнения сортировки требуется произвести.

Входные данные: в первой строке записано натуральное N, не превышающее 26 - количество букв латинского алфавита,
которые могут встречаться в сортируемом массиве. Далее в N строках через пробел записаны заглавная латинская буква и
число, соответствующее порядку этой буквы с точки зрения Пети. Далее - строка из заглавных латинских букв,
по длине не превышающая 100, для которой требуется посчитать число перестановок при сортировке пузырьком по возрастанию

Выходные данные: число перестановок элементов.

Пример:
Входные данные Выходные данные
3
A 3
B 2            3
Z 1
ABZ
"""