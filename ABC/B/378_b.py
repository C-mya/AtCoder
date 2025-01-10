N = int(input())
trash_list = []
for i in range(N):
    q, r = map(int, input().split(" ")) # 日付をqiで割ったあまりがriの日に収集されます
    trash_list += [(q, r)]

Q = int(input())
for i in range(Q):
    t, d = map(int, input().split(" "))
    if d % trash_list[t - 1][0] == trash_list[t - 1][1]: # 当日に回収
        print(d)
    elif d % trash_list[t - 1][0] < trash_list[t - 1][1]: # 現在のあまりがrより小さい場合
        print(d + trash_list[t - 1][1] - d % trash_list[t - 1][0])
    elif d % trash_list[t - 1][0] > trash_list[t - 1][1]: # 現在のあまりがrより大きい場合
        print(d - d % trash_list[t - 1][0] + trash_list[t - 1][1] + trash_list[t - 1][0])

# 無理やりすぎる