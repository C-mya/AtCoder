N = int(input())
X = []
Y = []
for i in range(N):
    a, b = list(map(int, input().split()))
    X += [a]
    Y += [b]

for i in range(N):
    max_l = 0
    ans = 0
    for j in range(N):  
        l = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
        if l > max_l:
            max_l = l
            ans = j + 1
    print(ans)


