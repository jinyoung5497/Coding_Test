from sys import stdin
from collections import deque
import heapq

test_num = int(stdin.readline().strip())
files = []

for _ in range(test_num):
    num = int(input())
    files = list(map(int, stdin.readline().strip().split()))
    heapq.heapify(files)
    answer = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        answer += a + b
        heapq.heappush(files, a + b)

    print(answer)
