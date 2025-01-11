N = int(input())
mochi = list(map(int, input().split(" ")))
count = 0

for i in range(N):
    for j in range(i + 1, N):
        if mochi[j] / 2 >= mochi[i]:
            count += N - j
            break
        else:
            continue


print(count)
