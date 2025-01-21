N, T, P = list(map(int, input().split(" ")))
L = list(map(int, input().split(" ")))

L.sort(reverse=True)
flag = True
count = 0
while flag:
    if L[P - 1] >= T:
        flag = False
    else:
        L = [x+1 for x in L]
        count += 1

print(count)
