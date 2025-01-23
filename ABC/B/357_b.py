S = input()
upper_count = 0

for i in range(len(S)):
    if S[i].isupper():
        upper_count += 1

if upper_count > len(S) // 2:
    print(S.upper())
else:
    print(S.lower())
