from sys import stdin
from collections import deque

num = int(stdin.readline().strip())
students = [list(map(int, stdin.readline().strip().split()))for _ in range(num)]
queue = deque()
length = 0
min_num = []

for i in students:
    if i[0] == 1:
        queue.append(i[1])
    elif i[0] == 2:
        queue.popleft()
    if len(queue) > length:
        length = len(queue)
        if min_num:
            min_num = []
        min_num.append(queue[-1])
    elif len(queue) == length:
        min_num.append(queue[-1])

print(length, min(min_num))