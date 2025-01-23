N, X, Y, Z = list(map(int, input().split(" ")))
A_math = list(map(int, input().split(" ")))
B_english = list(map(int, input().split(" ")))

pass_list = []
# math
A_sort = sorted(A_math, reverse=True)
for i in A_sort[:X]:
    a = A_math.index(i)
    pass_list += [a + 1]
    A_math[a] = -101
    B_english[a] = -101

# English
B_sort = sorted(B_english, reverse=True)
for i in B_sort[:Y]:
    b = B_english.index(i)
    pass_list += [b + 1]
    A_math[b] = -101
    B_english[b] = -101

# total

total = []
for i in range(N):
    total += [A_math[i] + B_english[i]]

total_sort = sorted(total, reverse=True)
for i in total_sort[:Z]:
    c = total.index(i)
    pass_list += [c + 1]
    total[c] = -202

pass_list.sort()
print(*pass_list, sep="\n")
