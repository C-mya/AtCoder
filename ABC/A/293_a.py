s = str(input())
ans = ""
for i in range(0, int(len(s)), 2):
    ans += (s[i + 1] + s[i])

print(ans)
    