a, b = list(map(int, input().split(" ")))
if a == b:
    print(-1)
else:
    for i in range (3):
        if a != i + 1 and b != i + 1:
            print(i + 1)


### 模範解答 ###
'''
A, B = map(int, input().split())
if A == B:
    print(-1)
else:
    print(A ^ B)
'''

# 排他的論理和！！！！！
