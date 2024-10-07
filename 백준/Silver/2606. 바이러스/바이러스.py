from sys import stdin
from collections import deque

computers = int(stdin.readline())
networks = int(stdin.readline())
connections = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)

for _ in range(networks):
    a, b = map(int, stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

def bfs(connections, visited):
    start = 1
    queue = deque()
    queue.append(start)
    count = 0
    visited[start] = True
    while queue:
        new_node = queue.popleft()
        for i in connections[new_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count


print(bfs(connections, visited))