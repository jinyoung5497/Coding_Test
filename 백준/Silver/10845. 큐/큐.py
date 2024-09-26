from collections import deque
from sys import stdin
num = int(stdin.readline())
d = deque()
# order = [stdin.readline().split() for _ in range(num)]

for _ in range(num):
    order = stdin.readline().split()
    if order[0] == 'push':
        d.append(order[1])
    elif order[0] == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif order[0] == 'size':
        print(len(d))
    elif order[0] == 'empty':
        if len(d) > 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif order[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
