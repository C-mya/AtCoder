A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

ab = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
bc = ((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
ca = ((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)

l = [ab, bc, ca]
l.sort()

if l[2] == l[0] + l[1]:
    print("Yes")
else:
    print("No")
