N = int(input())
A_list = []
for i in range(N):
    A_list += [list(map(int, input().split(" ")))]

now = 0
for i in range(N):  
    if int(now) >= i:
        now = A_list[int(now)][i]
    else:
        now = A_list[i][int(now)]
    print(i, now)
print(now)
