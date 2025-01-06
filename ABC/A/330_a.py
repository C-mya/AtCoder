n, l = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
clear = 0
for i in range(n):
    if a[i] >= l:
        clear += 1
print(clear)
