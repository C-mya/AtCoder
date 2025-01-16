h, w, d = list(map(int, input().split(" ")))
floor = []
wet = 0
dot_list = []

for i in range(h):
    floor += [str(input())]
    for j in range(w):
        if floor[i][j] == ".":
            dot_list += [(i, j)]

for i in range(len(dot_list)):
    if abs(floor[i][0] - floor[i + 1][0]) + abs(floor[i][1] - floor[i + 1][1]) 

print(dot_list)