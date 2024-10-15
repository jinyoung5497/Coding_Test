from collections import deque

def solution(maps):
    answer = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    start = (0, 0, 1)
    queue = deque([start])
    visited[0][0] = True
    while queue:
        y, x, count = queue.popleft()
        for dy, dx in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx, count + 1))
                if ny == len(maps) - 1 and nx == len(maps[0]) - 1:
                    return count + 1

    return -1