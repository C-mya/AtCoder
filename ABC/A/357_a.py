n, m = list(map(int, input().split(" ")))
h = list(map(int, input().split(" ")))
done = 0
for i in range(n):
    if m >= h[i]:
        done += 1
        m = m - h[i]
    else:
        break
print(done)
