X, Y, N = list(map(int, input().split(" ")))
count_1 = 0

count_1 += (N // 3) * Y
count_1 += (N - N // 3 * 3) * X

count_2 = 0
count_2 += N * X

print(min(count_1, count_2))
