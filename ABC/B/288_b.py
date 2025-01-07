n, k = list(map(int, input().split(" ")))
s_list = []
for i in range(n):
    s_list += [str(input())]

ans = sorted(s_list[:k])

print(*ans, sep="\n")

