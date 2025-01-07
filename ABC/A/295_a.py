n = int(input())
w = list(input().split(" "))
for i in range (n):
    if w[i] in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()
print("No")
