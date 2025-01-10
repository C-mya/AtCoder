n, q = list(map(int, input().split(" ")))

now_L = 1
now_R = 2
count = 0

for i in range(q):
    h, t = input().split(" ")
    t = int(t)
    if h == "R":
        if t == now_R: # その場から動かなくて良い
            count += 0
        else

        now_R = t

    elif h == "L":
        if t == now_L: # その場から動かなくて良い
            count += 0
        

        now_L = t
    
    print(now_L, now_R)

print(count)
