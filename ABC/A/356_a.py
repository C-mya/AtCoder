n, l, r = list(map(int, input().split(" ")))
# 数列Aは長さl
a = []
for i in range(1, n + 1):
    a += [i]
r_a = a[l-1:r]
r_a.reverse()

ans = a[:l-1] + r_a + a[r:]
ans = " ".join([str(n) for n in ans])

print(ans)
