X = int(input())
import math

for i in range(100000000):
    if math.factorial(i) == X:
        print(i)
        break
    

