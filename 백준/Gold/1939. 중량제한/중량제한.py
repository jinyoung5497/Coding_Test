from sys import stdin, setrecursionlimit
from collections import deque

n, m = map(int, stdin.readline().split())
island = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    island[a].append([b, c])
    island[b].append([a, c])

fac1, fac2 = map(int, stdin.readline().split())


def bfs(weight_limit):
    visited = [False] * (n + 1)
    queue = deque([fac1])
    visited[fac1] = True

    while queue:
        node = queue.popleft()

        if node == fac2:
            return True

        for next_node, limit in island[node]:
            if not visited[next_node] and limit >= weight_limit:
                visited[next_node] = True
                queue.append(next_node)

    return False


# 이진 탐색 범위 설정
low, high = 1, 1000000000
result = low

while low <= high:
    mid = (low + high) // 2
    if bfs(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

# 결과 출력
print(result)