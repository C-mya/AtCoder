import numpy as np

N = int(input())
P = list(map(int, input().split(" ")))
Q = list(map(int, input().split(" ")))
Q = np.array(Q)


ans = []
for i in range(N):

    a = np.argwhere(Q == i + 1)
    a = a.tolist()
    a = sum(a, []) # i + 1のインデックス
    
    p = P[a[0]] # i + 1のゼッケンをつけている人が見つめている人の番号を取得
    ans += [Q[p - 1]]

print(*ans)
