from collections import deque
from sys import stdin
r, c = map(int, input().split())
field = [list(stdin.readline().strip()) for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = {'k': 0, 'v': 0}
visited = [[False] * c for _ in range(r)]


def bfs(y, x, symbol):
    count = {'k': 0, 'v': 0}
    if symbol == "#":
        return
    elif symbol != "#" and symbol != '.' and not visited[y][x]:
        count[symbol] += 1
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < r and not visited[new_y][x] and field[new_y][x] != "#":
                if field[new_y][x] != '.':
                    count[field[new_y][x]] += 1
                q.append((new_y, x))
                visited[new_y][x] = True
            if 0 <= new_x < c and not visited[y][new_x] and field[y][new_x] != "#":
                if field[y][new_x] != '.':
                    count[field[y][new_x]] += 1
                q.append((y, new_x))
                visited[y][new_x] = True
    if count['v'] >= count['k']:
        answer['v'] += count['v']
    else:
        answer['k'] += count['k']


for i in range(r):
    for j in range(c):
        bfs(i, j, field[i][j])

print(*answer.values())

