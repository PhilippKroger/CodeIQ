L = 1
N = int(input())
R = N - 1
if N == 2 or N == 3:
    print(-1)
elif R % 5 == 0:
    print(R // 5)
else:
    print(R // 5 + 1)