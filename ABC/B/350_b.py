N, Q = list(map(int, input().split(" ")))
T = list(map(int, input().split(" ")))
not_tooth = []
for i in range(Q):
    if T[i] not in not_tooth:
        not_tooth += [T[i]]
    else:
        not_tooth.remove(T[i])

print(N - len(not_tooth))
