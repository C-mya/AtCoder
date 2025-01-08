n, r = list(map(int, input().split(" ")))

for i in range(n):
    d, a = list(map(int, input().split(" ")))
    if 2800 < r or r < 1200: # コンテストを経てもレーディングが変化しない
        break
    elif d == 1 and 1600 <= r <= 2799:
        r += a
    elif d == 2 and 1200 <= r <= 2399:
        r += a

print(r)

