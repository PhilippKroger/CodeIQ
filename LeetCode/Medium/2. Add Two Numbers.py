def addTwoNumbers(l1, l2):
    l1 = list(reversed(l1))
    L1 = ''
    for i in range(len(l1)):
        L1 += str(l1[i])
    L1 = int(L1)
    l2 = list(reversed(l2))
    L2 = ''
    for i in range(len(l2)):
        L2 += str(l2[i])
    L2 = int(L2)
    L = L1 + L2
    L = list(str(L)[::-1])
    L = list(map(int, L))
    return L


l1 = [2,4,3]
l2 = [5,6,4]
print(addTwoNumbers(l1, l2))
