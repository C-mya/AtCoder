h = int(input())
day = 1
plant = 1
for i in range(10000):
    if h >= plant:
        day += 1
        plant += 2 ** (i + 1)
    else:
        break
print(day)

### 模範解答 ###
'''
h=int(input())
now=0
ans=0
while now<=h:
    now+=1<<ans
    ans+=1

print(ans)
'''

# while文ね....
