s = input()
count_1 = 0
count_2 = 0
count_3 = 0
if s[0:6] == "1" or "2" or "3":
    for i in range(6):
        if s[i] == "1":
            count_1 += 1
        elif s[i] == "2":
            count_2 += 1
        elif s[i] == "3":
            count_3 += 1
        
    if count_1 == 1 and count_2 == 2 and count_3 == 3:
        print("Yes")    
    else:
        print("No")    
else:
    print("No")



