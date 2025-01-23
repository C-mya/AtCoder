N, A = list(map(int, input().split(" ")))
T = list(map(int, input().split(" ")))

now = 0
for i in range(N):
    if T[i] >= now: # 待たない
        print(T[i] + A)
        now = T[i] + A
    elif T[i] < now: # 待つ      
        print(now + A)
        now = now + A
    