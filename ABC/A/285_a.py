a, b = list(map(int, input().split(" ")))

tree_list = [[1, 2, 4, 8], [1, 2, 4, 9], [1, 2, 5, 10], [1, 2, 5, 11], [1, 3, 6, 12], [1, 3, 6, 13], [1, 3, 7, 14], [1, 3, 7, 15]]

for i in range(8):
    for j in range(3):
        if tree_list[i][j] == a:
            if tree_list[i][j + 1] == b:
                print("Yes")
                exit()
        elif tree_list[i][j] == b:
            if tree_list[i][j + 1] == a:
                print("Yes")
                exit()
print("No")

### 模範解答 ###
'''
a,b=map(int,input().split())
if a==b//2:
  print("Yes")
else:
  print("No")
'''

# なるほど
