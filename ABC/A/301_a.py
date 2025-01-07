n = int(input())
s = str(input())

Takahashi = 0
Aoki = 0

for i in range(n):
    if s[i] == "T":
        Takahashi += 1
    elif s[i] == "A":
        Aoki += 1

if Takahashi > Aoki:
    print("T")
elif Aoki > Takahashi:
    print("A")
else:
    if s[len(s) - 1] == "T":
        print("A")
    else:
        print("T")
