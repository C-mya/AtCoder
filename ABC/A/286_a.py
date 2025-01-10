N, P, Q, R, S = list(map(int, input().split(" ")))
a_list = input().split(" ")

top = a_list[P - 1:Q]
bottom = a_list[R - 1:S]

ans = a_list[:P - 1] + bottom + a_list[Q: R - 1] + top + a_list[S:]
print(*ans, sep=" ")
