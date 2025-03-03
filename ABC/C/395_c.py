import collections

N = int(input())
A = list(map(int, input().split()))
dupple_nunmber = []
dupple_nunmber = [k for k, v in collections.Counter(A).items() if v > 1]

# 重複がない場合
if dupple_nunmber == []:
    print("-1")
    exit()

dupple_count = {}

for i in range(N):
    # if A[i] in dupple_nunmber: # TLEネックポイント
    if A[i] in dupple_count:
        if dupple_count[A[i]][0] == 0 or dupple_count[A[i]][0] > i - dupple_count[A[i]][1]:
            dupple_count[A[i]][0] = i - dupple_count[A[i]][1] + 1
        
        dupple_count[A[i]][1] = i
    
    else:
        dupple_count[A[i]] = [0, i] # min_len, last_indexで初期化


ans = 0
for i in dupple_count:
    if dupple_count[i][0] != 0:
        if ans == 0 or ans > dupple_count[i][0]:
            ans = dupple_count[i][0]

print(ans)


# できた！！！！！！！！！！！
