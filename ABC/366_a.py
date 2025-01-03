n, t, a = list(map(int, input().split(" ")))
# 残り票数
x = n - (t + a)
if t - a > x or a - t > x:
  print("Yes")
else:
  print("No")
