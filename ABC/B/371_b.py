N, M = list(map(int, input().split(" ")))
men_house = []
for i in range(M):
    A, B = list(input().split(" "))
    if B == "M" and A not in men_house:
        print("Yes")
        men_house += [A]
    else:
        print("No")
