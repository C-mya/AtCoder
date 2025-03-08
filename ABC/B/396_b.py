Q = int(input())
now = [0] * 100
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        now += [query[1]]
    else:
        popped = now.pop(-1)
        print(popped)


                 

