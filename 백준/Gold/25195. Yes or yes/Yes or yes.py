from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

n, m = map(int, stdin.readline().split())
road = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    road[a].append(b)

int(stdin.readline())
fan_num = list(map(int, stdin.readline().split()))
isFan = False
def dfs(node):
    global isFan

    if node in fan_num:
        return

    if not road[node]:
        isFan = True
        return

    for i in road[node]:
        if road[node]:
            dfs(i)
        elif not road[node] and node not in fan_num:
            isFan = True


dfs(1)

if isFan:
    print("yes")
else:
    print("Yes")