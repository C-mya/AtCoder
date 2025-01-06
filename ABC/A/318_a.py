n, m, p = list(map(int, input().split(" ")))
ans = 0
if n >= m:
    for i in range(m, 1000000000, p):
        if n >= i:
            ans += 1
        else:
            break
print(ans)
            
