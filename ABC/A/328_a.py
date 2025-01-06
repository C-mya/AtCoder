n, x = list(map(int, input().split(" ")))
s = list(map(int, input().split(" ")))
total = 0
for i in range(n):
    if s[i] <= x:
        total += s[i]

print(total)
