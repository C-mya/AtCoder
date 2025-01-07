n = int(input())
s = str(input())
ans = "Yes"
for i in range(n - 1):
    if s[i] == s[i + 1]:
        ans = "No"
        break

print(ans)
