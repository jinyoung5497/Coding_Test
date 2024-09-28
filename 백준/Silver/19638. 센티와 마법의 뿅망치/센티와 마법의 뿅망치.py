import heapq
from sys import stdin
num, height, limit = list(map(int, stdin.readline().split()))
giant_height = [-int(stdin.readline()) for _ in range(num)]
count = 0
heapq.heapify(giant_height)

for _ in range(limit):
    if -giant_height[0] < height or -giant_height[0] == 1:
        break
    else:
        heapq.heapreplace(giant_height, -(-giant_height[0] // 2))
        count += 1

if -giant_height[0] >= height:
    print("NO")
    print(-giant_height[0])
else:
    print("YES")
    print(count)
