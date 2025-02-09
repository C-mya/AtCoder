S = list(input())
S.sort()

S_ = set(S)
count_list = []

for i in S_:
    count_list += [S.count(i)]

count_set = set(count_list)
ans = []

for i in count_set:
    ans += [count_list.count(i)]

for i in ans:
    if i != 0 and i != 2:
        print("No")
        exit()

print("Yes")
