s = list(map(int, input().split(" ")))
ans = "No"
for i in range(len(s) - 2):
    if 100 <= s[len(s) - 1] <= 675 and s[len(s) - 1] % 25 == 0:
        if s[i] <= s[i + 1]:
            if 100 <= s[i] <= 675 and s[i] % 25 == 0:
                ans = "Yes"
            else:
                ans = "No"
                break
        else:
            ans = "No"
            break
    else:
        ans = "No"
        break

print(ans)

### 模範解答 ###
'''
s = list(map(int, input().split()))

for i in range(8):
    # 順序が非増加でない場合
    if i < 7 and s[i] > s[i + 1]:
        print("No")
        exit()
    # 値が範囲外または25で割り切れない場合
    if s[i] < 100 or s[i] > 675 or s[i] % 25 != 0:
        print("No")
        exit()

print("Yes")
'''
# exit ...!!!!
