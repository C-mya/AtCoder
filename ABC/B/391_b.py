N, M = list(map(int, input().split(" ")))
S = []
T = []
for i in range(N):
    S += [input()]
for i in range(M):
    T += [input()]
flag = 0
if M == 1:
    for i in range(N): # 列
        for j in range(N): # 行
            if S[i][j] == T[0]:
                print(i + 1, j + 1)

else:
    for i in range(N - M + 1): # 列
        for j in range(N - M + 1): # 行

            for m in range(M):
                start = i + m
                if S[start][j:j + M] == T[m]:
                    flag += 1
            if flag == M:
                print(i + 1, j + 1)
                flag = 0
            else:
                flag = 0

        