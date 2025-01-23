N = int(input())
name = []
total = 0
for i in range(N):
    a, b = input().split(" ")
    name += [a]
    total += int(b)

name.sort()

print(name[total % N])
