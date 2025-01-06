n = int(input())
s = str(input())
ans = 0
A = 0
B = 0
C = 0
for i in range(n):
    if s[i] == "A":
        A += 1
        if A != 0 and B != 0 and C != 0:
            ans = i + 1
            break
    elif s[i] == "B":
        B += 1
        if A != 0 and B != 0 and C != 0:
            ans = i + 1
            break
    elif s[i] == "C":
        C += 1
        if A != 0 and B != 0 and C != 0:
            ans = i + 1
            break

print(ans)

### 模範解答 ###
'''
N = int(input())
S = input()

exist_a, exist_b, exist_c = False, False, False

for i in range(N):
  if S[i] == 'A': exist_a = True
  if S[i] == 'B': exist_b = True
  if S[i] == 'C': exist_c = True
  if exist_a and exist_b and exist_c:
    print(i + 1)
    break
'''

## TF判定、そう〜〜〜
