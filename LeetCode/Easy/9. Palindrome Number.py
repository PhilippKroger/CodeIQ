class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        c = len(x) // 2
        if len(x) % 2 == 0: x0, x1 = x[:c], x[c:]
        else:               x0, x1 = x[:c], x[c + 1:]
        rx1 = ''.join(reversed(x1))
        if x0 == rx1: return True
        else:         return False
