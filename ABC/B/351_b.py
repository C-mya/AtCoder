N = int(input())
A = []
B = []
for i in range(N):
    A += [input()]
for i in range(N):
    B += [input()]

for i in range(N):
    if A[i] != B[i]:
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i + 1, j + 1)
                exit()

