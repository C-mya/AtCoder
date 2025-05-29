S = list(input())
ans = 0
if len(S) % 2 == 1:
    S += "o"
    ans += 1
now = "o"
for i in range(len(S)):
    if S[i] == now:
        ans += 1
        if S[i] == "o":
            now = "i"
        else:
            now = "o"
    else:
        now = S[i]

print(ans)

?

