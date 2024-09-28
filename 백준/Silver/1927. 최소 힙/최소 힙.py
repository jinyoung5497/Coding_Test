from sys import stdin
import heapq

num = int(input())
numbers = [int(stdin.readline().strip()) for _ in range(num)]
new_numbers = []

for i in numbers:
    if i > 0:
        heapq.heappush(new_numbers, i)
    else:
        if new_numbers:
            print(heapq.heappop(new_numbers))
        else:
            print(0)