s = str(input())
a = 0
b = 0
c = 0

for i in range(3):
    if s[i] == "A":
        a += 1
    elif s[i] == "B":
        b += 1
    elif s[i] == "C":
        c += 1

if a == b == c == 1:
    print("Yes")
else:
    print("No")
