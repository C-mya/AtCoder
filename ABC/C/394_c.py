# S = input()
# flag = True
# while flag:
#     S = S.replace("WA", "AC")
#     if "WA" not in S:
#         flag = False

# print(S)
## TLE

S = list(input())
n = len(S)
now = 0

while now < n - 1:
    if S[now] == "W" and S[now + 1] == "A":
        S[now] = "A"
        S[now + 1] = "C"
        if now > 0:
            now -= 1
    else:
        now += 1

print(*S, sep="")


# def transform_string(s):
#     s = list(s) # listにすると文字列の変更が可能になる
#     n = len(s)
#     cur = 0
    
#     while cur < n - 1:
#         if s[cur] == 'W' and s[cur + 1] == 'A':
#             s[cur] = 'A'
#             s[cur + 1] = 'C'
#             if cur > 0:
#                 cur -= 1
#         else:
#             cur += 1
    
#     return "".join(s) # 文字列にして返す

# if __name__ == "__main__":
#     s = input().strip()
#     print(transform_string(s))
