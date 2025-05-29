N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    a = len(set(A[:i + 1]))
    b = len(set(A[i + 1:]))
    if a + b > ans:
        ans = a + b

print(ans)

# TLE

