s = str(input())

flag = 0
con = 0
ans = []

for i in range(len(s)):
    if s[i] == "|" and flag == 0:
        flag = 1
    elif s[i] == "-" and flag == 1:
        con += 1
    elif s[i] == "|" and flag == 1:
        ans += [con]
        con = 0

print(*ans, sep=" ")
