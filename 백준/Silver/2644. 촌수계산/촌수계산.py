from sys import stdin

n = int(stdin.readline())
x, y = map(int, stdin.readline().split())
m = int(stdin.readline())
relationship = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    relationship[a].append(b)
    relationship[b].append(a)


def dfs(x, y, relationship, visited, count):
    visited[x] = True
    for i in relationship[x]:
        if not visited[i]:
            if i == y:
                return count + 1
            result = dfs(i, y, relationship, visited, count + 1)
            if result != -1:
                return result
    return -1


print(dfs(x, y, relationship, visited, 0))