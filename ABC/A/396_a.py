N = int(input())
A = list(map(int, input().split()))

a = A[0]
cnt = 1
for i in range(1, N):
    if a == A[i]:
        cnt += 1
    else:
        cnt = 1
        a = A[i]
    if cnt == 3:
        print("Yes")
        exit()

print("No")
