N, M = list(map(int, input().split()))
l = []
count = 0

for i in range(M):
    X = sorted(list(map(int, input().split())))

    if X[0] == X[1] or X in l:
        count += 1
    else:
        l += [X]

print(count)

# TLE

