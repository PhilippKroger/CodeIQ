x = int(input())
y = int(input())
M = min(x, y)
N = max(x, y)
if M%2==0:
    m=2
else:
    m=1
r = M-m
n=N-r
print(n*m)