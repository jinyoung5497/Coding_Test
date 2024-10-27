from collections import deque

def solution(n, wires):
    network = [[] for _ in range(n + 1)]
    visited_node = []
    for i in range(len(wires)):
        network[wires[i][0]].append(wires[i][1])
        network[wires[i][1]].append(wires[i][0])

    for index in range(1, len(network)):
        visited = [False for _ in range(n + 1)]
        if len(wires) < index:
            break
        broken_node = wires[index - 1]
        queue = deque()
        queue.append(index)
        visited[index] = True
        while queue:
            first_node = queue.popleft()
            for j in network[first_node]:
                if not visited[j]:
                    if first_node not in broken_node or j not in broken_node:
                        visited[j] = True
                        queue.append(j)
        visited_node.append(sum(visited))

    # 1 1 3 8 8 6 8 8
    # 8 8 6 1 1 3 1 1
    # 7 7 3 7 7 3 7 7
    not_visited_node = []
    answer = []
    for i in visited_node:
        not_visited_node.append(n - i)
    for i in range(len(not_visited_node)):
        answer.append(abs(visited_node[i] - not_visited_node[i]))
    return min(answer)