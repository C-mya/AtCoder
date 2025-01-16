S = input()
T = input()
ans = 0
if S != T:
    for i in range(min([len(S), len(T)])):
        if S[i] != T[i]:
            ans = i + 1
            print(ans)
            exit()
    ans = min([len(S), len(T)]) + 1

print(ans)
        
