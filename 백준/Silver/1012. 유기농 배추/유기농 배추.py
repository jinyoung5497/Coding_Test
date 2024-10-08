from sys import stdin
from collections import deque

test_num = int(stdin.readline())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(test_num):
    x1, y1, k = map(int, stdin.readline().split())
    field = [[0] * x1 for _ in range(y1)]
    visited = [[False] * x1 for _ in range(y1)]
    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        field[b][a] = 1

    def bfs(y, x):
        if field[y][x] == 0:
            return
        queue = deque()
        queue.append((y, x))
        visited[y][x] = True
        while queue:
            new_y, new_x = queue.popleft()
            for dy, dx in directions:
                ny, nx = new_y + dy, new_x + dx
                if 0 <= ny < y1 and 0 <= nx < x1 and not visited[ny][nx] and field[ny][nx] == 1:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    count = 0
    for i in range(y1):
        for j in range(x1):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)