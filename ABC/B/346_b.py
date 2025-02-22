S = "wbwbwwbwbwbw" * 20
W, B = list(map(int, input().split()))
part_S = []
ans = "No"
for i in range(len(S) - W - B):
    part_S += [S[i:i + W + B]]

for i in range(len(part_S)):
    if part_S[i].count("w") == W:
        if part_S[i].count("b") == B:
            ans = "Yes"
            break
print(ans)
