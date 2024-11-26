from collections import deque
from sys import stdin

input = stdin.readline

n, m, start = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i in nodes:
    i.sort()

dfs_list = []
bfs_list = []

def dfs(input):
    dfs_list.append(input)
    visited[input] = True
    for i in nodes[input]:
        if not visited[i]:
            dfs(i)

def bfs(input):
    queue = deque([input])
    visited[input] = True
    while queue:
        new_node = queue.popleft()
        bfs_list.append(new_node)
        for i in nodes[new_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(start)
visited = [False for _ in range(n + 1)]
bfs(start)
print(*dfs_list)
print(*bfs_list)
