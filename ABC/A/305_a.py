n = int(input())
near = 0
for i in range(0, 101, 5):
    if n >= i:
        near = i
    else:
        if n - near < i - n:
            break
        else:
            near = i
            break
print(near)
