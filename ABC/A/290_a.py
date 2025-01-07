n, m = list(map(int, input().split(" ")))
a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))
total = 0
for i in b_list:
    total += a_list[i - 1]
print(total)
