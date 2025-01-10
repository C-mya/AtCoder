s_list = []
for i in range(8):
    s_list += [str(input())]

count = 0
j_list = []
for i in range(8):
    if "#" in s_list[i]:
        for j in range(8):
            if s_list[i][j] == "#":
                j_list += [j]
    else:
        count += 1

print((8 - len(set(j_list))) * count)
