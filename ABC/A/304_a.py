# n = int(input())
# dic_as = {}
# for i in range(n):
#     s, a = list(map(str, input().split(" ")))
#     dic_as[s] = int(a)

# dic_sorted = sorted(dic_as.items(), key=lambda x:x[1])
# dic_sorted = dict((x, y) for x, y in dic_sorted)
# ans = ""
# for i in dic_sorted:
#     print(i)

n = int(input())
s_list = []
a_list = []
for i in range(n):
    s, a = input().split(" ")
    s_list += [s]
    a_list += [int(a)]

min_index = a_list.index(min(a_list))
ans = s_list[min_index:] + s_list[:min_index]
print(*ans, sep="\n")
