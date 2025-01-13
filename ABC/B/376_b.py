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
        else:
            if t < now_L< now_R:
                count += n - now_R + t
            elif now_R < now_L < t:
                count += n - t + now_R
            else:
                count += abs(now_R - t)
        now_R = t

    elif h == "L":
        if t == now_L: # その場から動かなくて良い
            count += 0
        else:
            if now_L < now_R < t:
                count += n - t + now_L
            elif t < now_R < now_L:
                count += n - now_L + t
            else:
                count += abs(t - now_L)
        now_L = t

print(count)
