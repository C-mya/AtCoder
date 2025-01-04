l, r = list(map(int, input().split(" ")))
count = 0
for i in range (l, r+1):
    i = str(i)
    length = len(i)
    count_i = 0
    for j in range(1, length):
        if i[0] > i[j]:
            count_i += 1
    if count_i == length - 1:
        count += 1

print(count)

## 実行時間エラー
