n = int(input())
s = str(input())
ans = ""
for i in range(len(s)):
    ans += str(s[i]) * (int(2 * n / len(s)))
print(ans)
