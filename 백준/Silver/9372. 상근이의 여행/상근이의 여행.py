from collections import deque
from sys import stdin

testCase = int(input())

for _ in range(testCase):
    n, m = map(int, stdin.readline().split())
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
    print(n - 1)

