s = str(input())
ans = "Yes"
for i in range(16): # range(1, 16, 2)にすれば下のifは省略できる
    if (i + 1) % 2 == 0: 
        if s[i] != "0":
            ans = "No"
            break

print(ans)

