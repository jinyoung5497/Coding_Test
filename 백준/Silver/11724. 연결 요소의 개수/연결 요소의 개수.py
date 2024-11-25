from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
nodes = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        current_node = queue.popleft()
        for i in nodes[current_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)