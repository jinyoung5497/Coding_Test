from sys import stdin
from itertools import product

input = stdin.readline

n = int(input())
test = [int(input()) for _ in range(n)]
num = [1, 2, 3]
for i in test:
    count = 0
    for j in range(i):
        pos = product(num, repeat=j+1)
        for p in pos:
            if sum(p) == i:
                count += 1
    print(count)

