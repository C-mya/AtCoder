n, h, x = list(map(int, input().split(" ")))
p = list(map(int, input().split(" ")))

ans = 0
now_min = 0

for i in range(n):
    if p[i] >= x - h:
        if now_min == 0 or now_min > p[i]:
            now_min = p[i]
            ans = i + 1

print(ans)
