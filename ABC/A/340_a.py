a, b, d = list(map(int, input().split(" ")))
# 初項a, 末項b, 交差d
l = (b - a) / d + 1 # 項数
ans = []
for i in range(int(l)):
    ans.append(a + d * i)
print(*ans)

### 模範解答 ###
'''
A,B,D = map(int,input().split())
print(*range(A,B+1,D))
'''

# こんなことできるの！？
