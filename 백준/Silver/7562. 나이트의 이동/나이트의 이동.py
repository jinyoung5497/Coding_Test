from sys import stdin
from collections import deque

test_num = int(stdin.readline())
directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

def bfs(edge, s1, s2, e1, e2, directions):
    visited = [[False for _ in range(edge)] for _ in range(edge)]
    queue = deque([(s1, s2, 0)])
    if s1 == e1 and s2 == e2:
        return 0
    while queue:
        y, x, count = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < edge and 0 <= nx < edge and not visited[ny][nx]:
                if ny == e1 and nx == e2:
                    return count + 1
                visited[ny][nx] = True
                queue.append((ny, nx, count + 1))

for _ in range(test_num):
    edge = int(stdin.readline())
    s1, s2 = map(int, stdin.readline().split())
    e1, e2 = map(int, stdin.readline().split())
    print(bfs(edge, s1, s2, e1, e2, directions))


