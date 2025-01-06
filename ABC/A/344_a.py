s = str(input())
ans = ""
pipe = 0

for i in range(len(s)):
    if s[i] != "|" and pipe == 0:
        ans += s[i]
    elif s[i] == "|":
        if pipe == 0:
            pipe = 1
        elif pipe == 1:
            pipe = 0
print(ans)

### 模範解答 ### 
'''
S = input()
a, b, c = S.split('|')
print(a+c)
'''

## そりゃそう〜〜〜〜＾！！！！！

### 模範解答2 ###
'''
import re
S = input()
print(re.sub("\|.*\|", "", S))
'''

# 正規表現できるんか
