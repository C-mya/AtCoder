N = int(input())
S = []
length = 0
for i in range(N):
    S += [input()]
    if length < len(S[i]):
        length = len(S[i])
for i in range(N):
    if length > len(S[i]):
        S[i] += "*" * (length - len(S[i]))

ans = ""
for i in range(length):
    for j in reversed(range(N)):
        ans += S[j][i]
    flag = True
    while flag:
        if ans[-1] == "*":
            ans = ans[:-1]
        else:
            flag = False
    print(ans)
    ans = ""
