n, k, x = list(map(int, input().split(" ")))
a = list(map(str, input().split(" ")))

b = []
b = a[:k] + [str(x)] + a[k:]
b_ = " ".join(b)
print(b_)

### 模範解答 ###
'''
n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.insert(k,x)
print(*a)
'''

# insert！？
