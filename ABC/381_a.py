# input
n = int(input())
a = input()

l = int((n + 1) / 2 - 1)
# 偶奇
if n % 2 == 1:
  # aの真ん中が/か
  if a[l] == "/":
    if len(a) == 1:
      print("Yes")
    elif a[0:l] == "1"*len(a[0:l]) and a[l + 1:n] == "2"*len(a[0:l]):
      print("Yes")
    else:
      print("No")
  else:
    print("No")
else:
  print("No")
