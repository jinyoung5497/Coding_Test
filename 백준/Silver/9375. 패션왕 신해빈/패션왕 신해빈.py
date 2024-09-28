from sys import stdin
import math

num = int(stdin.readline().strip())
clothes = {}
value = []
for _ in range(num):
    n = int(stdin.readline().strip())
    for _ in range(n):
        s = stdin.readline().split()
        if s[1] in clothes:
            clothes[s[1]] += 1
        else:
            clothes[s[1]] = 1
    for i in clothes.values():
        i += 1
        value.append(i)
    print(math.prod(value) - 1)
    clothes = {}
    value = []


