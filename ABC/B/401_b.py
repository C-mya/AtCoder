N = int(input())
S = []
for i in range(N):
    S += [input()]

now = ""
count = 0

for i in range(N):
    if i == 0:
        now = S[i]
    if now != "login":
        if S[i] == "private":
            count += 1
    if S[i] == "login":
        now = "login"
    elif S[i] == "logout":
        now = "logout"

print(count)
