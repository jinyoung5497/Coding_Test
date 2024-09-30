from collections import deque
from sys import stdin
num = int(input())
field = [list(map(int, stdin.readline().strip().split())) for _ in range(num)]
answer = False

def bfs(y, x):
    global answer
    q = deque()
    q.append((y, x))
    visited = [[False] * num for _ in range(num)]
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        steps = field[y][x]
        new_y, new_x = y + steps, x + steps
        if steps == -1:
            answer = True
            return
        if 0 <= new_y < num and not visited[new_y][x]:
            q.append((new_y, x))
            visited[new_y][x] = True
        if 0 <= new_x < num and not visited[y][new_x]:
            q.append((y, new_x))
            visited[y][new_x] = True



bfs(0,0)

if answer:
    print("HaruHaru")
else:
    print("Hing")
