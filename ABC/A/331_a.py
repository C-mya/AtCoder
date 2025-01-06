M, D = list(map(int, input().split(" ")))
y, m, d = list(map(int, input().split(" ")))
ans = []
if d == D:
    if m == M:
        ans += (y + 1), 1, 1
    else:
        ans += y, (m + 1), 1
else:
    ans += y, m, (d + 1)

print(*ans, sep=" ")
