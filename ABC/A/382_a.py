n, d = list(map(int, input().split(" ")))
s = str(input())

kara = 0

for i in range(n):
    if s[i] == ".":
        kara += 1

print(kara + d)
