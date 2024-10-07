from sys import stdin
from collections import deque
import heapq

farm = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * 10 for _ in range(10)]
answer = []
for _ in range(10):
    farm.append(list(stdin.readline().strip()))

def bfs(farm, y, x, count):
    start = (y, x, count)
    queue = deque([start])
    visited[y][x] = True
    while queue:
        y, x, count = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 10 and 0 <= nx < 10 and not visited[ny][nx] and farm[ny][nx] != 'R' and farm[ny][nx] != 'L' and farm[ny][nx] != 'B':
                visited[ny][nx] = True
                queue.append((ny, nx, count + 1))
            if 0 <= ny < 10 and 0 <= nx < 10 and farm[ny][nx] == 'L':
                heapq.heappush(answer, count)


for i in range(len(farm)):
    for j in range(len(farm)):
        if farm[i][j] == 'B':
            bfs(farm, i, j, 0)

print(heapq.heappop(answer))