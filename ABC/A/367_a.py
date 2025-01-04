a, b, c = list(map(int, input().split(" ")))
# a時に叫ぶ, b時に就寝, c時に起床
if b > c:
  if c < a and a < b:
    print("Yes")
  else:
    print("No")
else:
  if c < a or a < b:
    print("Yes")
  else:
    print("No")
