N, K = list(map(int, input().split(" ")))
A_list = list(map(int, input().split(" ")))

ans = []
if K == 0:
    ans += A_list
elif N > K:
    ans += A_list[-(N - K):]
    ans += [0] * (N - len(ans))
elif N <= K:
    ans += [0] * N

print(*ans, sep=" ")
