a = input().split(" ")
a = list(map(int, a))
# 昇順にする
a.sort()
# 2個ペア
if a[0] == a[1] and a[2] == a[3]:
  print("Yes")
# 3:1
elif a[0] == a[1] == a[2]:
  print("Yes")
# 1:3
elif a[1] == a[2] == a[3]:
  print("Yes")
else:
  print("No")
