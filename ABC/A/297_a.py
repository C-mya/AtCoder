n, d = list(map(int, input().split(" ")))
t_list = list(map(int, input().split(" ")))
ans = -1
for i in range(n - 1):
    if t_list[i + 1] - t_list[i] <= d:
        ans = t_list[i + 1]
        break

print(ans)
