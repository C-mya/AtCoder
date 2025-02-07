# S = input()
# T = list(input())
# ans = []
# a = 0
# for i in range(len(S)):
#     index = T.index(S[i])
#     ans += [a + index + 1]
#     del T[:index + 1]

#     a = ans[i]

# print(*ans)

## TLE

## 以下GPT
s = input().strip()
t = input().strip()
n = len(s)
m = len(t)
a = [0] * n
j = 0

for i in range(m):
    if j < n and s[j] == t[i]:
        a[j] = i + 1
        j += 1

print(" ".join(map(str, a)))
