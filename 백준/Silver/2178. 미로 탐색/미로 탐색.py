from sys import stdin
from collections import deque

n, m = map(int, input().split())
maze = []
visited = [[0 for _ in range(m)] for _ in range(n)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for _ in range(n):
    maze.append(list(input()))

def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1
    while queue:
        new_y, new_x = queue.popleft()
        if new_y == n - 1 and new_x == m - 1:
            return visited[new_y][new_x]
        for dx, dy in directions:
            nx, ny = new_x + dx, new_y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] != '0' and visited[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = visited[new_y][new_x] + 1


print(bfs(0, 0))