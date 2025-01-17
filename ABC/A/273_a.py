N = int(input())
ans = 1
for i in range(N):
    ans *= (N - i)

print(ans)
