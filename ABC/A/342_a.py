s = str(input())
l = len(s)
ans = 0

for i in range(l - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        ans = 0
    else:
        if s[i] == s[i + 1]:
            ans = i + 2
            break
        elif s[i] == s[i + 2]:
            ans = i + 1
            break
        else:
            ans = i
            break

print(ans + 1)
