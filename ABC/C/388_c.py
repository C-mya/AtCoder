N = int(input())
mochi = list(map(int, input().split(" ")))
count = 0

for i in range(N):
    for j in range(i + 1, N):
        if mochi[j] / 2 < mochi[i]:
            continue
        else:
            count += N - j
            break

print(count)
# TLE

