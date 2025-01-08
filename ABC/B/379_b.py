n, k = list(map(int, input().split(" ")))
s = str(input())
con = 0
ans = 0
for i in range(n):
    if s[i] == "O":
        con += 1
        if con == k:
            ans += 1
            con = 0
    elif s[i] == "X":
        con = 0
print(ans)
