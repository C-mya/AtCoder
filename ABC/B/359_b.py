N = int(input())
A = list(map(int, input().split(" ")))
count = 0
for i in range(N):
    i_1 = A.index(i + 1)
    A[i_1] = 0
    i_2 = A.index(i + 1)

    if i_2 - i_1 == 2:
        count += 1

print(count)
