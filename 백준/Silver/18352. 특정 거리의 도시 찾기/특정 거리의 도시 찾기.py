from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
road = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

def bfs(road, visited, x):
    visited[x] = 0
    queue = deque()
    queue.append(x)
    while queue:
        new_node = queue.popleft()
        for i in road[new_node]:
            if visited[i] == 0:
                visited[i] = visited[new_node] + 1
                queue.append(i)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    road[a].append(b)

for i in road:
    i.sort()

bfs(road, visited, x)
empty = True
for i in range(len(visited)):
    if visited[i] == k and i != x:
        print(i)
        empty = False
if empty:
    print(-1)