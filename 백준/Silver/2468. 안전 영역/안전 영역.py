from sys import stdin
from collections import deque

n = int(stdin.readline())
field = []

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(n):
    field.append(list(map(int, stdin.readline().split())))

flatField = [i for n in field for i in n]
max_height = max(flatField)

count_safe_area_list = []

def bfs(startY, startX, flood_height):
    queue = deque([(startY, startX)])
    visited[startY][startX] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            new_y, new_x = dy + y, dx + x
            if 0 <= new_y < n and 0 <= new_x < n and field[new_y][new_x] >= flood_height and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                queue.append((new_y, new_x))


for flood_height in range(1, max_height + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count_safe_area = 0
    for i in range(n):
        for j in range(n):
            if field[i][j] >= flood_height and not visited[i][j]:
                bfs(i, j, flood_height)
                count_safe_area += 1
    count_safe_area_list.append(count_safe_area)

print(max(count_safe_area_list))