N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A_count = [0] * M
for i in range(N):
    X = list(map(int, input().split(" ")))
    for j in range(M):
        A_count[j] += X[j]
ans = "Yes"
for i in range(M):
    if A[i] > A_count[i]:
        ans = "No"
        break

print(ans)
