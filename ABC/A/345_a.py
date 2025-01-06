s = str(input())
l = len(s)

if (s[0] != "=") and (s[l - 1] != "="):
    if s[0] != s[l - 1]:
        if s[1:(l - 1)] == "=" * (l - 2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

### 模範解答 ###
'''
s=input()
flag=True
if s[0]!='<':
    flag=False
if s[-1]!='>':
    flag=False
for i in range(1,len(s)-1):
    if s[i]!='=':
        flag=False
if flag:
    print("Yes")
else:
    print("No")
'''

# なるほど...
