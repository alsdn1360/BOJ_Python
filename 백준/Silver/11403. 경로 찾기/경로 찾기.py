from collections import deque


def bfs(start):
    queue = deque([start])
    visited = [0] * n # 자기자신으로 오지 못 할수도 있으므로 visited[start] = 1 처리 하지 않음

    while queue:
        curr_node = queue.popleft()

        for nxt_node in g[curr_node]:
            if visited[nxt_node] == 0:
                queue.append(nxt_node)
                visited[nxt_node] = 1

    return visited


# main
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]

g = {node: [] for node in range(n)}

for i, edge in enumerate(edges):
    for j, is_edge in enumerate(edge):
        if is_edge:
            g[i].append(j)

for start in range(n):
    print(*bfs(start))
