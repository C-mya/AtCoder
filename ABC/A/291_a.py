s = str(input())
for i in range(int(len(s))):
    if s[i].isupper():
        print(i + 1)
        break
    