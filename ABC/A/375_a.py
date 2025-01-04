# n = int(input())
# s = str(input())
# count = 0
# for i in range(n - 2):
#     if s[i] and s[i + 2] == "#":
#         if s[i + 1] == ".":
#             count += 1

# print(count)
n = int(input())
s = str(input())
count = 0
for i in range(n - 2):
    if s[i] == "#" and s[i + 2] == "#" and s[i + 1] == ".":
        count += 1

print(count)
