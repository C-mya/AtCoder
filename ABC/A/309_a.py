a, b = list(map(int, input().split(" "))) # a < b
ans = "No"
if a in [1, 2, 4, 5, 7, 8]:
    if b == a + 1:
        ans = "Yes"

print(ans)
