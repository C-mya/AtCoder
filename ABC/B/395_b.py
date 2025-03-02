N = int(input())
l = [[0] * N for _ in range(N)]
# l = [[0] * N] * N  # これだと各行が独立しない
for i in range(1, N + 1):
    j = N + 1 - i

    if i <= j:
        if i % 2 == 1:
            for a in range(i - 1, j):
                for b in range(i - 1, j):
                    l[a][b] = "#" 
        else:
            for a in range(i - 1, j):
                for b in range(i - 1, j):
                    l[a][b] = "."

    else:
        continue

for i in range(N):
    print(*l[i], sep="")
