S, T = input().split(" ")
print(S[0:2])

if len(T) == 1:
    print("No")
    exit()

start = 0

for i in range(1, len(S)):
    for j in range(1, len(S) // i, i):
        print(i, j)
        # print(S[start:j])
        # start += j
    start = 0

if