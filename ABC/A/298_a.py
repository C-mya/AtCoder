n = int(input())
s = str(input())

count_o = 0

for i in range(n):
    if s[i] == "x":
        print("No")
        exit()
    elif s[i] == "o":
        count_o += 1

if count_o > 0:
    print("Yes")
else:
    print("No")
