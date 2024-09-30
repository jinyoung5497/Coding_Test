from collections import deque
r, c = map(int, input().split())
tiles = [list(input()) for _ in range(r)]
direction = [-1, 1]
answer = 0
def bfs(y, x):
    q = deque()
    q.append((y, x))

    if tiles[y][x] == '-':
        tiles[y][x] = '1'
        while q:
            y, x = q.popleft()
            for dx in direction:
                new_x = x + dx
                if 0 <= new_x < c and tiles[y][new_x] == '-':
                    q.append((y, new_x))
                    tiles[y][new_x] = '1'
    else:
        tiles[y][x] = '1'
        while q:
            y, x = q.popleft()
            for dy in direction:
                new_y = y + dy
                if 0 <= new_y < r and tiles[new_y][x] == '|':
                    q.append((new_y, x))
                    tiles[new_y][x] = '1'


for i in range(r):
    for j in range(c):
        if tiles[i][j] == '-' or tiles[i][j] == '|':
            bfs(i, j)
            answer += 1

print(answer)


