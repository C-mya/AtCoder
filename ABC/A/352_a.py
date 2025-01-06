n, x, y, z = list(map(int, input().split(" ")))
if x > y and x > z > y:
    print("Yes")
elif x < y and x < z < y:
    print("Yes")
else:
    print("No")
    