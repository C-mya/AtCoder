a, b, c, d, e, f = list(map(int, input().split(" ")))
g, h, i, j, k, l = list(map(int, input().split(" ")))

if a < g < d and b < h < e and c < i < f: # 右上奥
    print("Yes")
elif a < g < d and b < k < e and c < i < f: # 右上前
    print("Yes")
elif a < j < d and b < k < e and c < i < f: # 左上前
    print("Yes")
elif a < j < d and b < h < e and c < i < f: # 左上奥
    print("Yes")

if

elif a < g < d and b < k < e and c < l < f: # 右下前
    print("Yes")
elif a < g < d and b < h < e and c < l < f: # 右下奥
    print("Yes")
elif a < j < d and b < k < e and c < l < f: # 左下前
    print("Yes")
elif a < j < d and b < h < e and c < l < f: # 左下奥
    print("Yes")

else:
    print("No")
