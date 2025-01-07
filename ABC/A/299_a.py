n = int(input())
s = str(input())
flag = 0
in_bar = ""
for i in range(n):
    if s[i] == "|" and flag == 0:
        flag = 1
    elif s[i] != "|" and flag == 1:
        in_bar += s[i]
    elif s[i] == "|" and flag == 1:
        break

if "*" in in_bar:
    print("in")
else:
    print("out")
