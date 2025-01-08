n, d = list(map(int, input().split(" ")))
s = list(input())

cookie_list = [i for i, x in enumerate(s) if x == "@"]

for i in range(d):
    s[cookie_list[-i - 1]] = "."

print(*s, sep="")

### 模範解答 ### 
'''
n, d = map(int, input().split())
s = input()
for i in range(d):
    for j in range(n):
        if s[n - 1 - j] == '@':
            s = s[:n - 1 - j] + "." + s[n - j:]
            break
print(s)
'''

# う〜ん
