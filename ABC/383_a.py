n = int(input())
water = 0
mainus_water = 0

t_list = []
v_list =[]

for i in range(n):
    t_i, v_i = list(map(int, input().split(" ")))
    t_list.append(t_i)
    v_list.append(v_i)

for i in range(n-1):
    water += v_list[i]
    mainus_water += t_list[i+1] - t_list[i]
    if mainus_water < water:
        water = water - mainus_water
    else:
        water = 0
    mainus_water = 0

print(water + v_list[n-1])
