import collections

N = int(input())
A = list(map(int, input().split()))
dupple = []
dupple = [k for k, v in collections.Counter(A).items() if v > 1]

if dupple == []:
    print("-1")
    exit()

l = {}
for i in dupple:
    l[i] = 0

for i in range(N):
    if A[i] in dupple:
        if l[A[i]] == 0:
            l[A[i]] = i + 1
        else:
            l[A[i]] -= i + 1

print(abs(max(l.values())) + 1)

