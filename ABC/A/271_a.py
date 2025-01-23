N = int(input())

if len(hex(N)[2:]) == 2:
    print(hex(N)[2:].upper())
else:
    print("0" + hex(N)[2:].upper())
