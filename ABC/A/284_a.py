n = int(input())
s = []
for i in range(n):
    s += [input()]
s.reverse()
print(*s, sep="\n")
