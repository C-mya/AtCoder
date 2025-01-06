n, s, k = list(map(int, input().split(" ")))
total = 0

for i in range(n):
    p, q = list(map(int, input().split(" ")))
    total += p * q

if total >= s:
    print(total)
else:
    print(total + k)
