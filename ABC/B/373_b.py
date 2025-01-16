S = list(input())
count = 0
now = "A"

for i in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    count += abs(S.index(now) - S.index(i))
    now = i

print(count)
