H, W = list(map(int, input().split(" ")))
count = 0
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "#":
            count += 1
print(count)
