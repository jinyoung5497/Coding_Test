from sys import stdin

num = int(stdin.readline().strip())
buildings = list(map(int, stdin.readline().strip().split()))
level = [[] for _ in range(num)]


def tree(start, end, depth):
    if start == end:
        level[depth].append(buildings[start])
        return
    root_node = (start + end) // 2
    level[depth].append(buildings[root_node])
    tree(start, root_node - 1, depth + 1)
    tree(root_node + 1, end, depth + 1) 


tree(0, len(buildings) - 1,0)

for i in level:
    for j in i:
        print(j, end=" ")
    print()