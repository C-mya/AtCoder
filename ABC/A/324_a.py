n = int(input())
a = list(map(int, input().split(" ")))
if a == [a[0]] * n:
    print("Yes")
else:
    print("No")
