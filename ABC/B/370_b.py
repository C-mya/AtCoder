N = int(input())
A_list = []
for i in range(N):
    A_list += [list(map(int, input().split(" ")))]

now = 1
for i in range(N):  
    if int(now - 1) >= i:
        now = A_list[int(now) - 1][i]
    else:
        now = A_list[i][int(now) - 1]

print(now)
