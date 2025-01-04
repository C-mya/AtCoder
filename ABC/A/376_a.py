n, c = list(map(int, input().split(" ")))
t = list(map(int, input().split(" ")))
candy = 1 # 1回目は必ずキャンディがもらえる
candy_get_time = 0 # 1回目は必ずキャンディがもらえる

for i in range(1, n):
    if t[i] - t[candy_get_time] >= c:
        candy += 1
        candy_get_time = i

print(candy)
