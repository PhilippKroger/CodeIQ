r = int(input())
t = int(input())
k = int(input())
b = r*3 + t*2
while b >= k:
    b -= k
print(b)