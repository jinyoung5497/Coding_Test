from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

def bfs(a, b):
    q = deque()
    q.append([a, 0])
    visited[a] = True
    while q:
        new_node, total_distance = q.popleft()
        for value, distance in tree[new_node]:
            if not visited[value]:
                visited[value] = True
                if value == b:
                    return total_distance + distance
                q.append([value, total_distance + distance])



for _ in range(m):
    a, b = map(int, stdin.readline().split())
    visited = [False] * (n + 1)
    print(bfs(a, b))