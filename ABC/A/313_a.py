n = int(input())
p = list(map(int, input().split(" ")))
ans = 0
top = p[0]
for i in range(1, n):
    if p[i] >= top:
        ans = p[i] - p[0] + 1
        top = p[i]

print(ans)

### 模範解答 ###
'''
n = int(input())
p = list(map(int, input().split()))
m = 0
for i in range(1, n):
    m = max(m, p[i])
print(max(0, m + 1 - p[0]))
'''

# maxね.....
