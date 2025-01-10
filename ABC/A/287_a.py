n = int(input())
For = 0

for i in range(n):
    s = input()
    if s == "For":
        For += 1
    
if For >= n / 2:
    print("Yes")
else:
    print("No")
