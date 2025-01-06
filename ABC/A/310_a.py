n, p, q = list(map(int, input().split(" ")))
d = list(map(int, input().split(" ")))

ans = p

for i in range(n):
    if ans > (d[i] + q) or ans == 0:
        ans = d[i] + q

print(ans)
