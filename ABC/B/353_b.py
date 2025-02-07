N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

space = K
count = 0

for i in range(N):
    if A[i] <= space:
        space -= A[i]
    else:
        count += 1
        space = K - A[i]

print(count + 1)
