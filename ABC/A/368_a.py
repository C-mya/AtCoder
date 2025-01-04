n, k = list(map(int, input().split(" ")))
a =  input().split(" ")
new = []
new.append(a[-k:])
new.append(a[:-k])

new_str = " ".join(sum(new, []))
print(new_str)

### 模範解答 ### 
'''
N,K = map(int,input().split())
A = list(map(int,input().split()))
top = A[:-K]  # 上側
bottom = A[-K:]  # 下側
B = bottom + top  # 下側を上に持ってくる
print(*B)
'''

# リストの結合って+でできるんだ
