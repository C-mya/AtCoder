N, M = list(map(int, input().split()))
B_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

# b > w
B_list.sort(reverse=True)
W_list.sort(reverse=True)

value = 0
if value > W_list[0] + B_list[0]:
    print(0)
    exit()

# 正の数のみ、負の数のみのリストを作成
B_plus = []
B_minus = []
for i in range(N):
    if B_list[i] >= 0:
        B_plus += [B_list[i]]
    else:
        B_minus += [B_list[i]]

W_plus = []
W_minus = []
for i in range(M):
    if W_list[i] >= 0:
        W_plus += [W_list[i]]
    else:
        W_minus += [W_list[i]]


l = len(B_plus)
if len(B_plus) >= len(W_plus): # 正の数フルで使える時
    value = sum(B_plus) + sum(W_plus)
    print(value)
    exit()

else:
    value = sum(B_plus) + sum(W_plus[:l])
    if B_minus == []:
        print(value)
        exit()

    l_ = len(W_plus) - len(B_plus)
    if len(B_minus) >= l_:
        for i in range(l_):
            if value + B_minus[i] + W_plus[l + i] >= value:
                value += B_minus[i] + W_plus[l + i]
            else:
                print(value)
                exit()
        print(value)
        exit()

    else:
        for i in range(len(B_minus)):
            if value + B_minus[i] + W_plus[l + i] >= value:
                value += B_minus[i] + W_plus[l + i]
            else:
                print(value)
                exit()
        print(value)
        exit()
