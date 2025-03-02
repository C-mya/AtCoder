N = int(input())
A = list(map(int, input().split()))
a = 0
for i in range(N):
  if a < A[i]:
    a = A[i]
  else:
    print("No")
    exit()
print("Yes")
