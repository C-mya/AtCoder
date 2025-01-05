r, g, b = list(map(int, input().split(" ")))
c = str(input())
if c == "Red":
    if g >= b:
        print(b)
    else:
        print(g)
elif c == "Green":
    if r >= b:
        print(b)
    else:
        print(r)
elif c == "Blue":
    if r >= g:
        print(g)
    else:
        print(r)

### 模範解答 ###
'''
R, G, B = map(int, input().split())
C = input()
if C == "Red":
    print(min(G, B))
if C == "Green":
    print(min(B, R))
if C == "Blue":
    print(min(R, G))
'''

## min 知らんかった
