a, b, c = list(map(int, input().split(" ")))
if a == b == c:
  print("Yes")
elif a + b == c or a == b + c or b == a + c:
  print("Yes")
else:
  print("No")
