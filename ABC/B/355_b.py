N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

C = A + B
C.sort()

a_c = []
for i in range(N):
    a_c += [C.index(A[i])]

a_c.sort()
ans = "No"
for i in range(N - 1):
    if a_c[i + 1] - a_c[i] == 1:
        ans = "Yes"
        break

print(ans)
