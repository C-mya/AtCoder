n = str(input())
flag = "Yes"
for i in range(len(n) - 1):
    if int(n[i]) <= int(n[i + 1]):
        flag = "No"
        break

print(flag)
