from collections import deque
def solution(n, vertex):
    node = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for a, b in vertex:
        node[a].append(b)
        node[b].append(a)
    queue = deque([(1, 0)])
    visited[1] = True
    count_list = []
    while queue:
        node_num, count = queue.popleft()
        for i in node[node_num]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, count + 1))
        count_list.append(count)
    max_count = max(count_list)
    return count_list.count(max_count)