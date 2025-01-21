X = float(input())

if str(X).split(".")[1] == "0":
    X = str(X).split(".")[0]

print(X)
