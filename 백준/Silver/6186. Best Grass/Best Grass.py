from collections import deque
r, c = map(int, input().split())
pasture = [list(input()) for _ in range(r)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def bfs(y, x):
    q = deque()
    q.append((y, x))
    pasture[y][x] = '1'
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            Y, X = y + dy, x + dx
            if 0 <= Y < r and 0 <= X < c and pasture[Y][X] == '#':
                q.append((Y, X))
                pasture[Y][X] = '1'


for i in range(r):
    for j in range(c):
        if pasture[i][j] == '#':
            bfs(i, j)
            answer += 1

print(answer)


