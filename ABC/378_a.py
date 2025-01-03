a = list(map(int, input().split(" ")))
if a[0] == a[1]:
    if a[2] == a[3]:
        print("2")
    else:
        print("1")

elif a[0] == a[2]:
    if a[1] == a[3]:
        print("2")
    else:
        print("1")

elif a[0] == a[3]:
    if a[1] == a[2]:
        print("2")
    else:
        print("1")

elif a[1] == a[2]:
    print("1")

elif a[1] == a[3]:
    print("1")

elif a[2] == a[3]:
    print("1")

else:
    print("0")
           