n = int(input())
h = list(map(int, input().split(" ")))
ans = 0

for i in range(n): # 1, nにしたらn=1の時にWAになった　なるほど
    if h[0] >= h[i]:
        ans = -1
    else:
        ans = i + 1
        break

print(ans)
