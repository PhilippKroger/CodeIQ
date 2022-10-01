a = int(input())
h, m = list(map(int, input().split()))
print((((1-(m / 60)) * 360) + a + (h * (360 / 12)) + (360 / 12 * (m / 60))) % 360)