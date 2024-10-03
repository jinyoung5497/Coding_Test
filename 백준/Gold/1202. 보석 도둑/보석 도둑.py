from sys import stdin
import heapq

a, b = map(int, stdin.readline().split())
bag = []
weight = []

for _ in range(a):
    w, v = map(int, stdin.readline().split())
    bag.append((w, v))

for _ in range(b):
    weight.append(int(stdin.readline().strip()))

bag.sort()
weight.sort()

max_heap = []
answer = 0
index = 0

for w in weight:
    while index < len(bag) and bag[index][0] <= w:
        heapq.heappush(max_heap, -bag[index][1])
        index += 1

    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)