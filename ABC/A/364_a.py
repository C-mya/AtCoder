n = int(input())
sweet = 0
for i in range(n):
    s = str(input())
    if sweet <= 1 and i < (n-1):
        if s == "salty":
            sweet = 0
        elif s == "sweet":
            sweet += 1
    elif i < (n-1):
        sweet += 100
    
if sweet == 0 or sweet == 1:
    print("Yes")
else:
    print("No")
