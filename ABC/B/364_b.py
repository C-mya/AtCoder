H, W = list(map(int, input().split(" "))) # マトリクスの情報
S_i, S_j = list(map(int, input().split(" "))) # 現在地
S_i -= 1
S_j -= 1

C = [] # マトリクス
for i in range(H):
    C += [input()]
X = input() # コマンド

for i in range(len(X)):
    if X[i] == "L" and S_j != 0:
        if C[S_i][S_j - 1] == ".":
            S_j -= 1
    elif X[i] == "R" and S_j != W - 1:
        if C[S_i][S_j + 1] == ".":
            S_j += 1
    elif X[i] == "U" and S_i != 0:
        if C[S_i - 1][S_j] == ".":
            S_i -= 1
    elif X[i] == "D" and S_i != H - 1:
        if C[S_i + 1][S_j] == ".":
            S_i += 1

print(S_i + 1, S_j + 1)
