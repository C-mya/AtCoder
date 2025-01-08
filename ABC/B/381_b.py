# s = str(input())
# ans = "No"
# if len(s) % 2 == 0: # 長さが偶数
#     for i in range(int(len(s) / 2)):
#         if s[2 * i] == s[2 * i + 1]: # 連続する2文字が同一
#             if len(set(s)) == int(len(s) / 2): # 各文字2回ずつ出現
#                 ans = "Yes"

# print(ans)

s = str(input())
# 長さが偶数か
if len(s) % 2 != 0:
    print("No")
    exit()

# 条件を満たすかチェック
half_length = len(s) // 2
if len(set(s)) != half_length:  # 各文字が2回ずつ出現しているか
    print("No")
    exit()

# 各文字が連続しているか
for i in range(0, len(s), 2):
    if s[i] != s[i + 1]:  # 連続する2文字が異なる場合
        print("No")
        exit()

# すべての条件を満たす場合
print("Yes")
