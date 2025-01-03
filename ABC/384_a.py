n, c_1, c_2 = list(map(str, input().split(" ")))
n = int(n)
s = input()

out_list = []

for i in range(n):
    if s[i] == c_1:
        out_list.append(s[i])
    else:
        out_list.append(c_2)

print("".join(out_list))
