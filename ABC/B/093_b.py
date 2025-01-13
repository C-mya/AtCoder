A, B, K = list(map(int, input().split(" ")))
ans = []
if K >= B - A:
    K = B - A + 1
for i in range(K):
    ans += [A + i]
    ans += [B - i]

ans = sorted(list(set(ans)))
print(*ans, sep="\n")
