M = int(input())
ans = []
for i in reversed(range(11)):
    if M >= 3 ** i:
        ans += [i]
        M = M - 3 ** i
        if M >= 3 ** i:
            ans += [i]
            M = M - 3 ** i
    if M == 0:
        break


print(len(ans))
print(*ans, sep=" ")
