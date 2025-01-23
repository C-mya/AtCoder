N, Q = list(map(int, input().split(" ")))
L = []
for i in range(N):
    L += [list(map(int, input().split(" ")))]

ans = []
for i in range(Q):
    s, t = list(map(int, input().split(" ")))
    ans += [L[s - 1][t]]

print(*ans, sep="\n")
