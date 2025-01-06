n = int(input())
s = str(input())
ans = -1
for i in range(n-2):
    if s[i:i+3] == "ABC":
        ans = i + 1
        break
print(ans)
