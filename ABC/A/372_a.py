s = str(input())
l = len(s)
new = ""
for i in range(l):
    if s[i] != ".":
        new += s[i]
print(new)
