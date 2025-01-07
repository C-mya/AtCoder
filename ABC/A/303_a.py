n = int(input())
s = str(input())
t = str(input())

ans = "No"
for i in range(n):
    if s[i] != t[i]:
        if s[i] == "1" and t[i] == "l":
            ans = "Yes"
        elif s[i] == "l" and t[i] == "1":
            ans = "Yes"
        elif s[i] == "0" and t[i] == "o":
            ans = "Yes"
        elif s[i] == "o" and t[i] == "0":
            ans = "Yes"
        else:
            print("No")
            exit()
    else:
        ans = "Yes"
print(ans)
