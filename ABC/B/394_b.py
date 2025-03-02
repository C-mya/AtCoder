N = int(input())
S = []
for i in range(N):
    S += [input()]

S_ = sorted(S, key=len)
print(*S_, sep="")
