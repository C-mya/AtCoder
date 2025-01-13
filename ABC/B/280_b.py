N = int(input())
S_list = list(map(int, input().split(" ")))
ans = []
diff = 0

for i in range(N):
    ans += [S_list[i] - diff]
    diff += ans[i]

print(*ans, sep=" ")
