n, a, b = list(map(int, input().split(" ")))
c_list = list(map(int, input().split(" ")))

for i in range(n):
    if c_list[i] == (a + b):
        print(i + 1)
