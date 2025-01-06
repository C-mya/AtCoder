s = str(input())
boin = ["a", "e", "i", "o", "u"]
ans = ""
for i in range(len(s)):
    if s[i] not in boin:
        ans += s[i]

print(ans)

### 模範解答 ###
'''
import re
print(re.sub('a|e|i|o|u', '', input()))
'''

# 正規表現
