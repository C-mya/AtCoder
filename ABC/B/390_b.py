N = int(input())
A = list(map(int, input().split(" ")))

# if len(A) % 2 == 1:
#     if A[0] * A[-1] == A[len(A) // 2] ** 2:
#         print("Yes")
#     else:
#         print("No")
# elif len(A) % 2 == 0:
#     if A[0] * A[-1] == A[1] * A[-2]:
#         print("Yes")
flag = True
for i in range(N - 2):
    if A[i] * A[i + 2] != A[i + 1] * A[i + 1]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
    