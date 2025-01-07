h, w, x, y = list(map(int, input().split(" ")))
map_dict = {}
for i in range(h):
    map_dict[i] = str(input())
t = str(input())
list_xy = []
count = 0

for i in range(len(t)):
    if t[i] == "U" and map_dict[x - 2][y - 1] != "#":
        x -= 1
        if map_dict[x - 1][y - 1] == "@" and (x, y) not in list_xy:
            count += 1
            list_xy += [(x, y)]
    elif t[i] == "D" and map_dict[x][y - 1] != "#":
        x += 1
        if map_dict[x - 1][y - 1] == "@" and (x, y) not in list_xy:
            count += 1
            list_xy += [(x, y)]
    elif t[i] == "L" and map_dict[x - 1][y - 2] != "#":
        y -= 1
        if map_dict[x - 1][y - 1] == "@" and (x, y) not in list_xy:
            count += 1
            list_xy += [(x, y)]
    elif t[i] == "R" and map_dict[x - 1][y] != "#":
        y += 1
        if map_dict[x - 1][y - 1] == "@" and (x, y) not in list_xy:
            count += 1
            list_xy += [(x, y)]

print(x, y, count)

### 模範解答 ###
'''
H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)] # 2次元リストに格納
T = input()

X-=1
Y-=1
ans=0
for c in T:
  if c=='U' and S[X-1][Y]!='#': X-=1
  if c=='D' and S[X+1][Y]!='#': X+=1
  if c=='L' and S[X][Y-1]!='#': Y-=1
  if c=='R' and S[X][Y+1]!='#': Y+=1
  if S[X][Y]=='@':
    ans+=1
    S[X][Y]='.' # 1回通った家を破壊

print(X+1,Y+1,ans)
print(S)
'''