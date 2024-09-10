from collections import deque
d = deque()
input_num = int(input())
exe_list = [input().split() for _ in range(input_num)]

for i in exe_list:
    if i[0] == "push_back":
        d.append(i[1])
    elif i[0] == "push_front":
        d.appendleft(i[1])
    elif i[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif i[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    elif i[0] == "size":
        print(len(d))
    elif i[0] == "empty":
        if len(d) == 0:
            print(1)
        else: print(0)
    elif i[0] == "pop_front":
        if len(d) == 0:
            print(-1)
        else:
            # d.popleft()
            print(d.popleft())
    elif i[0] == "pop_back":
        if len(d) == 0:
            print(-1)
        else:
            # d.pop()
            print(d.pop())