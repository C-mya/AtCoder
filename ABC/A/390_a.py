A = list(map(int, input().split(" ")))
if A == [2, 1, 3, 4, 5] or A == [1, 2, 4, 3, 5] or A == [1, 2, 3, 5, 4] or A == [2, 3, 4, 5, 1] or A == [1, 3, 2, 4, 5]:
    print ("Yes")

else:
    print("No")
