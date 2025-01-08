h, w, d = list(map(int, input().split(" ")))
floor = []
wet = 0
for i in range(h):
    floor += [str(input())]

for i in range(h - d):
    for j in range(w - d):
        if i == 0:
            if floor[i][j] == ".":

# ???

