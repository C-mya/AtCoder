# 418 B

from mpmath import mp

mp.dps = 100
mp.pretty = True

S = input()
count_t = []
for i in range(len(S)):
    if S[i] == "t":
        count_t += [i]

ans = 0
if len(count_t) >= 3:
    a = mp.mpf(len(count_t) - 2)
    b = mp.mpf(count_t[-1] - count_t[0] + 1 - 2)
    ans = a / b
    print(mp.mpf(ans))
else:
    print(ans)


