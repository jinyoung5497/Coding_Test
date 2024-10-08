from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
max_num = 100000
visited = [False] * (max_num + 1)
def bfs(n, m):
    queue = deque()
    queue.append((n, 0))
    visited[n] = True
    while queue:
        new_node, count = queue.popleft()
        if new_node == m:
            return count
        for i in [-1, 1, new_node]:
            new_x = new_node + i
            if 0 <= new_x <= max_num and not visited[new_x]:
                visited[new_x] = True
                queue.append((new_x, count + 1))


print(bfs(n, m))
