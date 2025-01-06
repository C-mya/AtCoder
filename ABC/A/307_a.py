n = int(input())
a = list(map(int, input().split(" ")))
ans = []
for i in range(int(len(a) / 7)):
    week = 0
    for j in range(7):
        week += a[7*i + j]

    ans += [week]

print(*ans, sep=" ")
