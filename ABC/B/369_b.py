N = int(input())
tired = 0
L_now = 0
R_now = 0
for i in range(N):
    A, S = list(input().split(" "))
    A = int(A)
    if S == "R" and R_now == 0:
        R_now = A
    elif S == "R" and R_now != 0:
        tired += abs(A - R_now)
        R_now = A
    elif S == "L" and L_now == 0:
        L_now = A
    elif S == "L" and L_now != 0:
        tired += abs(A - L_now)
        L_now = A

print(tired)
