N, D = list(map(int, input().split(" ")))
t_l_list = []

for i in range(N):
    t, l = list(map(int, input().split(" ")))
    t_l_list += [(t, l)]

ans = []
for i in range(D):
    for k in range(N):
        ans += [t_l_list[k][0] * (t_l_list[k][1] + i + 1)]
    print(max(ans))
    ans = []

