H, W = list(map(int, input().split()))
S = []
for _ in range(H):
    S += [input()]

a, b, c, d = 0, 0, 0, 0
flag = True
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if flag and a == 0 and c == 0:
                a = i
                b = i
                c = j
                d = j
                flag = False
            else:
                if d <= j:
                    d = j
                if b <= i:
                    b = i


# 範囲内に白があった場合を判定
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if S[i][j] == ".":
            print("No")
            exit()

# 上
for i in range(a):
    for j in range(W):
        if S[i][j] == "#":
            print("No")
            exit()

# 下
for i in range(b + 1, H):
    for j in range(W):
        if S[i][j] == "#":
            print("No")
            exit()

# 左
for i in range(H):
    for j in range(c):
        if S[i][j] == "#":
            print("No")
            exit()

# 右
for i in range(H):
    for j in range(d + 1, W):
        if S[i][j] == "#":
            print("No")
            exit()


print("Yes")
