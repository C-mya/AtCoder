N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

ans = []
for i in range(N):
    if i + 1 not in A:
        ans += [i + 1]

print(len(ans))
print(*ans)

