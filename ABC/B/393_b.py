S = input()
count = 0
for i in range(len(S)):
    if S[i] == "A":
        for j in range(i + 1, len(S)):
            if S[j] == "B":
                for k in range(j + 1, len(S)):
                    if (j - i) == (k - j) and S[k] == "C":
                        count += 1

print(count)

