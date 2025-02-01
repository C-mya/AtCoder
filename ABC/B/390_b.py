# import math
# N = int(input())
# A = list(map(int, input().split(" ")))

# flag = True
# ans = "No"

# for i in range(N - 2):
#     while math.inclose(A[i + 1] / A[i], A[i + 2] / A[i + 1]):
#         ans = "Yes"

# print(ans)


# N = int(input())
# A = list(map(int, input().split(" ")))

# flag = True
# ans = "Yes"


if len(A) == 1:
    print("No")
    exit()
 
for i in range(len(A) - 2):
    if not A[i + 1] / A[i] == A[i + 2] / A[i + 1]:
        ans = "No"
        break

print(ans)

if 