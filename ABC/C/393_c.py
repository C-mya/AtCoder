# N, M = list(map(int, input().split()))
# l = []
# count = 0

# for i in range(M):
#     X = sorted(list(map(int, input().split())))

#     if X[0] == X[1] or X in l:
#         count += 1
#     else:
#         l += [X]

# print(count)

# # TLE

N, M = list(map(int, input().split(" ")))
ans = 0
edge_count = {}
edges = []
for i in range(M):
    edges += [tuple(map(int, input().split(" ")))]

for u, v in edges:
    if u == v:
        ans += 1
        continue
    if u > v:
        u, v = v, u
    edge_count[(u, v)] = edge_count.get((u, v), 0) + 1

for k in edge_count.values():
    ans += k - 1 # 1本は残していいから

print(ans)

