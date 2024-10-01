from sys import stdin

num = int(stdin.readline().strip())
buildings = [list(map(int, stdin.readline().strip().split())) for _ in range(num)]
stack = [0]
count = 0
buildings.append([0,0])

for i in buildings:
    height = i[1]
    while stack[-1] > i[1]:
        if stack[-1] != height:
            count += 1
            height = stack[-1]
        stack.pop()
    stack.append(i[1])
print(count)


