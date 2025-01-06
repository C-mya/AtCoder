n = int(input())
# x: 高橋, y: 青木
takahashi = 0
aoki = 0

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    takahashi += x
    aoki += y

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
