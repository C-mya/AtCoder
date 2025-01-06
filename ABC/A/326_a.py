x, y = list(map(int, input().split(" ")))
# x階からy階までの移動
if 0 < (y - x) <= 2:
    print("Yes")
elif -3 <= (y - x) < 0:
    print("Yes")
else:
    print("No")
