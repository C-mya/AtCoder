N = int(input())
x_n, y_n = 0, 0
cost = 0
for i in range(N):
    X, Y = list(map(int, input().split(" ")))
    cost += ((x_n - X) ** 2 + (y_n - Y) ** 2) ** 0.5
    x_n = X
    y_n = Y

cost += ((x_n) ** 2 + (y_n) ** 2) ** 0.5

print(cost)
