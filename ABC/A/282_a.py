K = int(input())
import string

s = string.ascii_uppercase
print(s[:K])

### 模範解答
'''k = int(input())
for i in range(k):
    print(chr(ord('A') + i), end = '')
'''
# chr!