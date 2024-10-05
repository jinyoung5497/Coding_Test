from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())
line = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    line[a].append(b)
    line[b].append(a)
for i in line:
    i.sort()
def bfs(t):
    global count
    visited[t] = count
    queue = deque([t])
    while queue:
        first_queue = queue.popleft()
        for i in line[first_queue]:
            if visited[i] == 0:
                count += 1
                queue.append(i)
                visited[i] = count

bfs(R)

for i in range(1, N + 1):
    print(visited[i])