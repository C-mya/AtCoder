s = str(input())
if s[0:3] == "ABC":
    if 1 <= int(s[3:6]) <= 349 and int(s[3:6]) != 316:
        print("Yes")
    else:
        print("No")
