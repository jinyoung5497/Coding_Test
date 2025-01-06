from sys import stdin
from collections import deque

input = stdin.readline

num = int(input())
graph = [list(map(int, input().strip())) for _ in range(num)]
visited = [[False for _ in range(num)] for _ in range(num)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = []

def bfs(y, x):
    count = 1
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        first_y, first_x = q.popleft()
        for dy, dx in direction:
            new_y, new_x = dy + first_y, dx + first_x
            if 0 <= new_y < num and 0 <= new_x < num and not visited[new_y][new_x] and graph[new_y][new_x] == 1:
                visited[new_y][new_x] = True
                q.append((new_y, new_x))
                count += 1
    answer.append(count)


for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(answer))
answer.sort()
for i in answer:
    print(i)