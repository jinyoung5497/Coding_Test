from sys import stdin

num = 5
numbers = [list(map(str, stdin.readline().split())) for _ in range(num)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = []
def bfs(y, x, number):
    if len(number) == 6:
        if number not in answer:
            answer.append(number)
        return

    for dy, dx in directions:
        new_y, new_x = dy + y, dx + x
        if 0 <= new_y < num and 0 <= new_x < num:
            bfs(new_y, new_x, number + numbers[new_y][new_x])


for i in range(num):
    for j in range(num):
        bfs(i, j, numbers[i][j])

print(len(answer))