N = int(input())
A = list(map(int, input().split(" ")))
flag = True
count = 0
while flag:
    A.sort(reverse=True)
    A[0] -= 1 
    A[1] -= 1
    count += 1
    if A.count(0) >= N - 1:
        flag = False
print(count)
