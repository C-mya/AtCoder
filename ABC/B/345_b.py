X = str(input())
if int(X) > 10:
    if X[-1] == "0":
        print(X[:-1])
    else:
        print(int(X[:-1]) + 1)
elif int(X) < -10:
    print(X[:-1])
elif -10 < int(X) <= 0:
    print(0)
else:
    print(1)
    