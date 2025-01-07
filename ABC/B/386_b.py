s = str(input())
count = 0
flag_0 = 0 # 0連続中か否か
count_0 = 0 # 0連続回数
for i in range(len(s)):
    if s[i] != "0":
        if flag_0 == 0: # 0連続とは無関係
            count += 1
        else: # 0連続終了地点
            if count_0 % 2 == 0:
                count += count_0 // 2 + 1
                count_0 = 0
                flag_0 = 0
            else:
                count += count_0 // 2 + 2
                count_0 = 0
                flag_0 = 0

    elif flag_0 == 0: # 0連続開始
        if i == (len(s) - 1): #最後の文字が0
            count += 1
        else:
            flag_0 = 1
            count_0 += 1
    elif flag_0 == 1: # 0連続中
        if i == (len(s) - 1): #最後の文字が0
            count_0 += 1
            if count_0 % 2 == 0:
                count += count_0 // 2 
            else:
                count += count_0 // 2 + 1
        else:
            count_0 += 1
print(count)
